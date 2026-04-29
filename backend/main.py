import os
import json
import httpx
import re
import asyncio
import random
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from openai import OpenAI, APIError, APIConnectionError, RateLimitError
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from database import engine, get_db
from models import Base, Itinerary, User
from config import settings
import logging
import traceback

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="VoyageAI API",
    description="智能旅行规划API",
    version="1.0.0"
)

# 创建数据库表
Base.metadata.create_all(bind=engine)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # 前端开发服务器
        "http://127.0.0.1:5173",
        "http://localhost:8080",
        "http://127.0.0.1:8080"
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# 初始化DeepSeek客户端
deepseek_client = None

DEEPSEEK_MODEL = "deepseek-chat"

async def get_city_adcode(city: str, client: httpx.AsyncClient) -> str:
    """获取城市的adcode（行政区划代码）"""
    try:
        url = f"https://restapi.amap.com/v3/geocode/geo?address={city}&key={settings.amap_api_key}"
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "1" and data.get("geocodes"):
                adcode = data["geocodes"][0]["adcode"]
                logger.info(f"成功获取{city}的adcode: {adcode}")
                return adcode
            else:
                logger.error(f"获取城市adcode失败: {data}")
                return None
        else:
            logger.error(f"获取城市adcode请求失败: {response.status_code}")
            return None
    except Exception as e:
        logger.error(f"获取城市adcode异常: {e}")
        return None

async def get_weather_data(city: str) -> dict:
    """调用高德地图API获取实时天气"""
    # 创建客户端配置，添加重试机制
    async with httpx.AsyncClient(
        trust_env=False,
        timeout=15.0,
        limits=httpx.Limits(max_keepalive_connections=5, max_connections=10),
        headers={
            "User-Agent": "VoyageAI/1.0",
            "Accept": "application/json"
        },
        follow_redirects=True
    ) as client:
        
        # 尝试多次连接
        for attempt in range(3):
            try:
                # 第一步：获取城市adcode
                adcode = await get_city_adcode(city, client)
                if not adcode:
                    logger.warning(f"无法获取{city}的adcode，返回模拟数据")
                    return {
                        "city": city,
                        "temp": "22°C",
                        "condition": "多云转晴",
                        "warning": "无法获取城市信息，当前显示模拟数据"
                    }
                
                # 第二步：获取实时天气数据
                weather_url = f"https://restapi.amap.com/v3/weather/weatherInfo?city={adcode}&key={settings.amap_api_key}"
                response = await client.get(weather_url)
                
                if response.status_code == 200:
                    data = response.json()
                    if data.get("status") == "1" and data.get("lives"):
                        live_data = data["lives"][0]
                        logger.info(f"成功获取{city}的天气数据：{live_data['temperature']}°C, {live_data['weather']}")
                        return {
                            "city": live_data.get("city", city),
                            "temp": f"{live_data['temperature']}°C",
                            "condition": live_data["weather"],
                            "humidity": live_data.get("humidity", "N/A"),
                            "wind_direction": live_data.get("winddirection", "N/A"),
                            "wind_power": live_data.get("windpower", "N/A"),
                            "warning": get_weather_warning(live_data)
                        }
                    else:
                        logger.error(f"天气数据解析失败: {data}")
                        if attempt < 2:
                            logger.info(f"等待2秒后重试...")
                            await asyncio.sleep(2)
                            continue
                        return {
                            "city": city,
                            "temp": "22°C",
                            "condition": "多云转晴",
                            "warning": "天气数据解析失败，当前显示模拟数据"
                        }
                else:
                    logger.error(f"天气API返回错误状态码：{response.status_code}")
                    if attempt < 2:
                        logger.info(f"等待2秒后重试...")
                        await asyncio.sleep(2)
                        continue
                    return {
                        "city": city,
                        "temp": "22°C",
                        "condition": "多云转晴",
                        "warning": f"天气数据获取失败 ({response.status_code})，当前显示模拟数据"
                    }
                    
            except httpx.ConnectTimeout:
                logger.error(f"天气API连接超时 (尝试 {attempt + 1}/3)")
                if attempt < 2:
                    logger.info(f"等待3秒后重试...")
                    await asyncio.sleep(3)
                    continue
                return {
                    "city": city,
                    "temp": "22°C",
                    "condition": "多云转晴",
                    "warning": "网络连接超时，当前显示模拟数据"
                }
            except httpx.ConnectError:
                logger.error(f"天气API连接错误 (尝试 {attempt + 1}/3)")
                if attempt < 2:
                    logger.info(f"等待3秒后重试...")
                    await asyncio.sleep(3)
                    continue
                return {
                    "city": city,
                    "temp": "22°C",
                    "condition": "多云转晴",
                    "warning": "网络连接错误，当前显示模拟数据"
                }
            except httpx.ReadTimeout:
                logger.error(f"天气API读取超时 (尝试 {attempt + 1}/3)")
                if attempt < 2:
                    logger.info(f"等待3秒后重试...")
                    await asyncio.sleep(3)
                    continue
                return {
                    "city": city,
                    "temp": "22°C",
                    "condition": "多云转晴",
                    "warning": "读取数据超时，当前显示模拟数据"
                }
            except httpx.HTTPError as e:
                logger.error(f"天气API HTTP错误: {e} (尝试 {attempt + 1}/3)")
                if attempt < 2:
                    logger.info(f"等待3秒后重试...")
                    await asyncio.sleep(3)
                    continue
                return {
                    "city": city,
                    "temp": "22°C",
                    "condition": "多云转晴",
                    "warning": f"天气服务异常，当前显示模拟数据"
                }
            except Exception as e:
                logger.error(f"天气API调用失败: {e} (尝试 {attempt + 1}/3)")
                if attempt < 2:
                    logger.info(f"等待3秒后重试...")
                    await asyncio.sleep(3)
                    continue
                return {
                    "city": city,
                    "temp": "22°C",
                    "condition": "多云转晴",
                    "warning": "天气服务异常，当前显示模拟数据"
                }

def get_weather_warning(weather_data: dict) -> str:
    """根据天气数据生成预警提示（适配高德地图数据格式）"""
    warnings = []
    
    # 从高德地图数据中提取信息
    temp = float(weather_data.get("temperature", 22))
    humidity = int(weather_data.get("humidity", 50))
    weather_desc = weather_data.get("weather", "").lower()
    wind_power = weather_data.get("windpower", "≤3")
    
    # 温度预警
    if temp > 30:
        warnings.append("高温预警，注意防暑降温。")
    elif temp < 5:
        warnings.append("低温预警，注意保暖。")
    
    # 天气状况预警
    if "雨" in weather_desc or "雪" in weather_desc:
        warnings.append("降水天气，请携带雨具或保暖装备。")
    elif "晴" in weather_desc:
        warnings.append("晴朗天气，紫外线较强，建议防晒。")
    elif "雾" in weather_desc or "霾" in weather_desc:
        warnings.append("能见度较低，注意交通安全。")
    
    # 湿度预警
    if humidity > 80:
        warnings.append("湿度较大，敏感人群请注意。")
    
    # 风力预警
    try:
        wind_level = int(wind_power.replace("≤", ""))
        if wind_level >= 6:
            warnings.append("风力较大，注意出行安全。")
    except:
        pass
    
    return " ".join(warnings) if warnings else "天气适宜出行。"

async def generate_itinerary(start: str, dest: str, days: int, budget: str) -> dict:
    """调用 DeepSeek 生成结构化行程（包含预算约束）"""
    
    # 如果DeepSeek客户端未初始化，直接返回模拟数据
    if deepseek_client is None:
        print("DeepSeek客户端未初始化，使用模拟数据")
        return build_realistic_mock_itinerary(start, dest, days, budget)
    
    prompt = f"""
你是一个专业的旅行规划师。请根据以下信息生成详细的行程规划：

- 出发地：{start}
- 目的地：{dest}
- 游玩天数：{days}
- 预算范围：{budget}人民币

请严格按照以下 JSON 格式返回，不要包含任何其他文字：
{{
  "overview": {{
    "destination": "{dest}",
    "days": {days},
    "budget": "{budget}",
    "best_season": "最佳旅行季节",
    "pace": "游玩节奏建议",
    "highlights_count": 核心体验数量
  }},
  "daily_plan": [
    {{
      "day": 1,
      "title": "当日主题",
      "activities": [
        {{
          "time": "时间段（例如 09:00-12:00）",
          "title": "活动名称（具体地点/街区）",
          "description": "详细描述（避免空话，给出动线/注意事项；请根据预算{budget}推荐合适消费）",
          "transport": "交通方式（地铁/步行/打车/公交/高铁等，给出建议）",
          "duration": "预计耗时（例如 2-3 小时）",
          "food": ["用餐推荐 1", "用餐推荐 2"],
          "alternatives": ["备选方案 1（下雨/人多/闭馆时）", "备选方案 2"],
          "booking_tip": "门票/预约提示（若需要预约，说明平台与提前多久）"
        }}
      ]
    }}
  ],
  "budget_breakdown": [
    {{ "category": "机票/交通", "amount": 金额 }},
    {{ "category": "酒店住宿", "amount": 金额 }},
    {{ "category": "美食餐饮", "amount": 金额 }},
    {{ "category": "门票娱乐", "amount": 金额 }}
  ],
  "packing_list": ["物品 1", "物品 2", ...]
}}
确保行程内容真实合理，符合{dest}的旅游特点，并且消费水平与预算{budget}匹配。
"""
    
    try:
        response = deepseek_client.chat.completions.create(
            model=DEEPSEEK_MODEL,
            messages=[
                {"role": "system", "content": "你是一个专业的旅行规划助手，只返回 JSON 格式数据。"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2000,
            temperature=0.7
        )
        
        content = response.choices[0].message.content
        print(f"DeepSeek响应内容: {content[:200]}...")  # 调试信息
        
        # 提取JSON部分
        json_start = content.find('{')
        json_end = content.rfind('}') + 1
        
        if json_start != -1 and json_end != -1:
            json_str = content[json_start:json_end]
            result = json.loads(json_str)
            
            # 添加模型信息
            result["model_info"] = {
                "model_used": DEEPSEEK_MODEL,
                "provider": "DeepSeek",
                "response_time": "N/A"
            }
            
            return result
        else:
            print("警告：模型返回内容不包含有效 JSON")
            raise ValueError("模型返回内容不包含有效 JSON")
            
    except Exception as e:
        print(f"DeepSeek API 调用失败：{e}")
        # 返回模拟数据
        return build_realistic_mock_itinerary(start, dest, days, budget)

# 目的地定制化数据库
DESTINATION_DATA = {
    "北京": {
        "best_season": "3-5月 / 9-11月",
        "pace": "适中偏紧凑",
        "highlights": 8,
        "daily_plan": [
            {"title": "皇城初探·中轴线巡礼", "activities": [
                {"time": "上午", "title": "天安门广场 & 故宫博物院", "description": "从天安门步行进入故宫，建议走中轴线+东西六宫路线，预留3-4小时。提前在「故宫博物院」小程序预约门票。"},
                {"time": "下午", "title": "景山公园俯瞰紫禁城", "description": "登上景山万春亭，360度俯瞰故宫全景，是北京最佳拍照点之一。"},
                {"time": "傍晚", "title": "南锣鼓巷漫步", "description": "在胡同里感受老北京烟火气，品尝炸酱面、卤煮、豆汁等地道小吃。"}
            ]},
            {"title": "长城壮志·中华文化", "activities": [
                {"time": "上午", "title": "慕田峪长城", "description": "比八达岭人少景美，建议缆车上山步行下山，感受万里长城的磅礴气势。"},
                {"time": "下午", "title": "明十三陵·定陵", "description": "探索明代皇家陵寝，感受历史的厚重与庄严。"},
                {"time": "傍晚", "title": "鸟巢 & 水立方夜景", "description": "奥林匹克公园夜景璀璨，适合拍照打卡。"}
            ]},
            {"title": "皇家园林·文艺胡同", "activities": [
                {"time": "上午", "title": "颐和园", "description": "昆明湖畔漫步长廊，登万寿山远眺，感受皇家园林的极致之美。"},
                {"time": "下午", "title": "圆明园遗址公园", "description": "在大水法遗址前感受历史的沧桑。"},
                {"time": "傍晚", "title": "798艺术区", "description": "当代艺术殿堂，各种画廊、咖啡馆和创意小店，文艺气息十足。"}
            ]},
            {"title": "市井烟火·地道京味", "activities": [
                {"time": "上午", "title": "天坛公园", "description": "看祈年殿、回音壁，感受明清皇家祭天文化的庄严。"},
                {"time": "下午", "title": "前门大街 & 大栅栏", "description": "逛百年老字号，瑞蚨祥、同仁堂、全聚德，体验老北京商业文化。"},
                {"time": "傍晚", "title": "什刹海酒吧街", "description": "在湖边酒吧小酌，听着驻唱歌手的民谣，结束完美旅程。"}
            ]}
        ],
        "packing": ["身份证（故宫/长城需实名）", "舒适运动鞋（长城步行必备）", "防晒霜（户外景点多）", "充电宝（全天拍照耗电大）", "保温杯（北京早晚温差大）"]
    },
    "上海": {
        "best_season": "3-5月 / 10-12月",
        "pace": "悠闲",
        "highlights": 7,
        "daily_plan": [
            {"title": "外滩璀璨·魔都初见", "activities": [
                {"time": "上午", "title": "豫园 & 城隍庙", "description": "江南古典园林代表，品尝南翔小笼、蟹壳黄等上海经典小吃。"},
                {"time": "下午", "title": "南京路步行街", "description": "中国第一商业街，从和平饭店一路逛到人民广场。"},
                {"time": "傍晚", "title": "外滩万国建筑群", "description": "黄浦江畔欣赏万国建筑博览会，等待陆家嘴灯光亮起的震撼瞬间。"}
            ]},
            {"title": "浦东风华·艺术之旅", "activities": [
                {"time": "上午", "title": "上海中心大厦观光", "description": "中国第一高楼118层观光厅，360度俯瞰魔都全貌。"},
                {"time": "下午", "title": "中华艺术宫（原世博会中国馆）", "description": "免费参观大型艺术展览，感受中国当代艺术的魅力。"},
                {"time": "傍晚", "title": "田子坊", "description": "石库门里弄改造的文艺街区，各种手作店、咖啡馆、画廊。"}
            ]},
            {"title": "法租界浪漫·小资生活", "activities": [
                {"time": "上午", "title": "武康路漫步", "description": "梧桐树荫下的法租界老洋房，武康大楼是必拍地标。"},
                {"time": "下午", "title": "思南公馆", "description": "花园洋房群中的露天咖啡馆，享受上海最慵懒的午后。"},
                {"time": "傍晚", "title": "新天地", "description": "石库门建筑群中的时尚餐饮聚集地，夜晚氛围最佳。"}
            ]}
        ],
        "packing": ["轻薄外套（室内空调冷）", "舒适步行鞋", "充电宝", "墨镜（拍照加分）", "雨伞（上海多阵雨）"]
    },
    "成都": {
        "best_season": "3-6月 / 9-11月",
        "pace": "悠闲",
        "highlights": 8,
        "daily_plan": [
            {"title": "熊猫之都·慢生活启程", "activities": [
                {"time": "上午", "title": "大熊猫繁育研究基地", "description": "8点前入园看大熊猫最活跃的进食时间！月亮产房可以看到小熊猫宝宝。"},
                {"time": "下午", "title": "宽窄巷子", "description": "清朝古街道改造的文化街区，掏耳朵、盖碗茶、三大炮，体验地道成都生活。"},
                {"time": "傍晚", "title": "人民公园喝盖碗茶", "description": "在鹤鸣茶社点一杯竹叶青，听旁边大爷摆龙门阵，感受成都慢生活精髓。"}
            ]},
            {"title": "三国遗韵·火辣美食", "activities": [
                {"time": "上午", "title": "武侯祠 & 锦里", "description": "三国圣地武侯祠，旁边的锦里古街是体验民俗和购买伴手礼的好去处。"},
                {"time": "下午", "title": "杜甫草堂", "description": "诗圣故居，竹林幽径中的文学圣地。"},
                {"time": "傍晚", "title": "建设路美食街", "description": "烤脑花、冒椒火辣、降龙爪爪……本地人最爱的深夜美食据点。"}
            ]},
            {"title": "都江古堰·青城仙山", "activities": [
                {"time": "上午", "title": "都江堰水利工程", "description": "两千年前的水利奇迹，鱼嘴、飞沙堰、宝瓶口三大工程令人叹为观止。"},
                {"time": "下午", "title": "青城山前山", "description": "道教名山，空气清新，登顶约2-3小时，感受'青城天下幽'。"},
                {"time": "傍晚", "title": "玉林路小酒馆", "description": "赵雷歌里的玉林路，走走停停，找个小酒馆坐坐，体验成都夜生活。"}
            ]}
        ],
        "packing": ["肠胃药（辛辣食物备需）", "防晒（紫外线强）", "雨伞（多阴雨）", "舒适运动鞋", "充电宝"]
    },
    "西安": {
        "best_season": "3-5月 / 9-11月",
        "pace": "紧凑",
        "highlights": 9,
        "daily_plan": [
            {"title": "千年古都·始皇雄风", "activities": [
                {"time": "上午", "title": "秦始皇兵马俑博物馆", "description": "世界第八大奇迹！建议请讲解员，一号坑的军阵令人震撼。提前在公众号预约。"},
                {"time": "下午", "title": "华清宫", "description": "唐明皇与杨贵妃的爱情圣地，体验《长恨歌》实景演出的震撼。"},
                {"time": "傍晚", "title": "回民街 & 洒金桥", "description": "肉夹馍、羊肉泡馍、biangbiang面……西安美食的灵魂就在这些小巷子里。"}
            ]},
            {"title": "城墙骑行·大唐不夜城", "activities": [
                {"time": "上午", "title": "西安古城墙", "description": "中国现存最完整的古城墙，租自行车骑行一圈约1.5小时，俯瞰古今交融的西安。"},
                {"time": "下午", "title": "陕西历史博物馆", "description": "十八件国宝级文物，从周秦汉唐到宋元明清，看完一部中国通史。需提前预约！"},
                {"time": "傍晚", "title": "大唐不夜城", "description": "亚洲最大唐文化主题步行街，灯火辉煌如梦回长安，不倒翁小姐姐在此。"}
            ]},
            {"title": "大雁塔·文艺长安", "activities": [
                {"time": "上午", "title": "大雁塔 & 大慈恩寺", "description": "玄奘法师翻译佛经之地，登塔远眺西安城区。"},
                {"time": "下午", "title": "大唐芙蓉园", "description": "中国最大的仿唐皇家建筑群，园内演出精彩，拍照效果极佳。"},
                {"time": "傍晚", "title": "永兴坊非遗美食街", "description": "摔碗酒、子长煎饼、陕北民歌，体验最地道的陕西非遗文化。"}
            ]}
        ],
        "packing": ["舒适运动鞋（城墙/兵马俑步行多）", "防晒霜", "充电宝", "身份证（多处实名预约）", "保温杯"]
    },
    "杭州": {
        "best_season": "3-5月 / 9-11月",
        "pace": "悠闲",
        "highlights": 7,
        "daily_plan": [
            {"title": "西湖十景·诗画江南", "activities": [
                {"time": "上午", "title": "断桥残雪 & 白堤", "description": "西湖最经典路线，沿白堤漫步至孤山，感受白娘子与许仙的爱情传说。"},
                {"time": "下午", "title": "灵隐寺", "description": "千年古刹，飞来峰石刻造像精美，寺内香火鼎盛。"},
                {"time": "傍晚", "title": "南山路 & 湖滨银泰", "description": "沿湖咖啡馆一条街，夕阳下的西湖美不胜收。"}
            ]},
            {"title": "龙井问茶·宋韵古街", "activities": [
                {"time": "上午", "title": "龙井村茶园", "description": "漫步茶园梯田，品一杯正宗龙井，感受采茶的乐趣。"},
                {"time": "下午", "title": "南宋御街 & 河坊街", "description": "仿古商业街，各种杭州特色小吃和手工艺品。"},
                {"time": "傍晚", "title": "西溪湿地", "description": "非诚勿扰拍摄地，摇橹船穿梭芦苇荡间，感受城市中的世外桃源。"}
            ]},
            {"title": "千岛碧水·良渚文明", "activities": [
                {"time": "上午", "title": "良渚古城遗址公园", "description": "五千年前中华文明曙光，世界文化遗产。"},
                {"time": "下午", "title": "中国美术学院象山校区", "description": "王澍普利兹克奖建筑作品，建筑与自然的完美融合。"},
                {"time": "傍晚", "title": "钱塘江夜景", "description": "灯光秀震撼人心，城市阳台是最佳观赏点。"}
            ]}
        ],
        "packing": ["雨伞（杭州多雨）", "舒适步行鞋", "防晒霜", "充电宝", "轻薄外套"]
    }
}

def _stable_rng(*parts: str) -> random.Random:
    seed = "|".join([p or "" for p in parts])
    # deterministic across restarts for same input
    return random.Random(seed)

def normalize_destination(dest: str) -> str:
    """Normalize ambiguous destinations into a concrete city."""
    d = (dest or "").strip()
    if not d:
        return d
    # Strip prompt tails accidentally included in destination
    # e.g. "北京玩5天" / "北京5日" / "东京自由行"
    d = re.sub(r'(?:玩|游玩|游|旅行|自由行|之旅)\s*\d+\s*(?:天|日).*$', '', d)
    d = re.sub(r'\d+\s*(?:天|日).*$', '', d)
    d = re.sub(r'(?:玩|游玩|游|旅行|自由行|之旅).*$', '', d)
    d = d.strip()
    # common aliases
    alias = {
        "日本": "东京",
        "Japan": "东京",
        "东京": "东京",
        "大阪": "大阪",
        "京都": "京都",
        "韩国": "首尔",
        "Korea": "首尔",
        "泰国": "曼谷",
        "Thailand": "曼谷",
    }
    return alias.get(d, d)

# A lightweight POI pool used when AI is unavailable. Keep it simple & realistic.
POI_DB = {
    "东京": {
        "best_season": "3-5月 / 10-12月",
        "pace": "适中",
        "highlights": 10,
        "areas": ["浅草", "上野", "银座", "涩谷", "新宿", "原宿表参道", "秋叶原", "台场"],
        "days": [
            {
                "title": "浅草·上野：传统与博物馆",
                "activities": [
                    {"time": "08:30-10:30", "title": "浅草寺 & 仲见世商店街", "description": "早到人少更好拍；顺路在仲见世买人形烧/雷门周边小吃。", "transport": "地铁至浅草站 + 步行", "duration": "约 2 小时", "food": ["浅草周边和菓子/人形烧", "雷门附近天妇罗/荞麦面"], "alternatives": ["下雨：改去浅草文化观光中心观景台", "人太多：改走花屋敷周边小路"], "booking_tip": "浅草寺无需预约；热门时段注意排队与人流。"},
                    {"time": "10:45-12:30", "title": "隅田公园散步（可选东京晴空塔外观）", "description": "步行衔接浅草区域；想登塔可提前预约时段票。", "transport": "步行/1 站地铁", "duration": "约 1.5 小时", "food": ["隅田川沿岸咖啡", "晴空塔商场轻食"], "alternatives": ["阴雨：改去晴空塔 Solamachi 商场", "想省钱：仅拍外观不登塔"], "booking_tip": "登晴空塔建议提前在官网/平台预约时段票。"},
                    {"time": "13:30-16:30", "title": "上野公园 & 博物馆二选一", "description": "推荐东京国立博物馆/国立西洋美术馆；行程别排太满，留体力。", "transport": "地铁至上野站 + 步行", "duration": "约 3 小时", "food": ["上野站周边拉面/定食", "公园周边便当+草地休息"], "alternatives": ["闭馆日：改去上野动物园/不忍池", "带孩子：优先动物园"], "booking_tip": "部分特展需预约或限流；出发前查看馆方官网。"},
                    {"time": "18:00-20:00", "title": "阿美横丁晚餐", "description": "海鲜丼/居酒屋很集中；饭点排队正常，预算适中可选连锁寿司或烧鸟。", "transport": "步行/地铁 10-20 分钟", "duration": "约 2 小时", "food": ["海鲜丼", "烧鸟/居酒屋小食"], "alternatives": ["不想排队：改去上野站内美食街", "想更安静：去御徒町小巷店"], "booking_tip": "多数店不预约，尽量错峰 17:30 或 20:00 后。"},
                ],
            },
            {
                "title": "涩谷·原宿：年轻潮流与街拍",
                "activities": [
                    {"time": "09:30-11:00", "title": "明治神宫晨间参拜", "description": "树林步道很治愈；参观约1小时，周末人多。"},
                    {"time": "11:15-13:00", "title": "原宿竹下通 & 表参道", "description": "甜品/潮店集中；喜欢安静可以走表参道支路。"},
                    {"time": "14:00-16:30", "title": "涩谷十字路口 & SHIBUYA SKY（可选）", "description": "观景台建议提前预约；不登台也可在周边商场/咖啡厅取景。"},
                    {"time": "18:00-20:30", "title": "涩谷/惠比寿晚餐", "description": "拉面/烧肉选择多；晚饭后可轻松逛街收尾。"},
                ],
            },
            {
                "title": "新宿·歌舞伎町：城市夜景与购物",
                "activities": [
                    {"time": "09:30-11:30", "title": "新宿御苑", "description": "适合慢走+拍照；花季需注意闭园日。"},
                    {"time": "12:00-13:30", "title": "新宿午餐（拉面/咖喱）", "description": "建议错峰；连锁店也很稳。"},
                    {"time": "14:00-17:30", "title": "新宿站周边百货/电器店购物", "description": "药妆、电器可集中采购；留意退税门槛与护照。"},
                    {"time": "19:00-21:00", "title": "都厅展望台夜景（免费）", "description": "相比收费观景台更省预算；若排队可改去周边高层咖啡厅。"},
                ],
            },
            {
                "title": "秋叶原·二次元补给",
                "activities": [
                    {"time": "10:00-12:30", "title": "秋叶原电器街漫逛", "description": "手办/中古店很多；先比价再下手。"},
                    {"time": "13:30-16:30", "title": "主题店/周边店打卡", "description": "按兴趣选择（动画、游戏、模型）；部分店铺周末拥挤。"},
                    {"time": "18:00-20:30", "title": "神田/秋叶原周边晚餐", "description": "想吃更地道可去神田小巷；不想折腾就选站内美食街。"},
                ],
            },
            {
                "title": "台场：海湾线与夜景",
                "activities": [
                    {"time": "10:00-12:00", "title": "台场海滨公园散步", "description": "晴天很出片；可看彩虹大桥与海湾景观。"},
                    {"time": "13:00-16:30", "title": "teamLab/商场二选一", "description": "teamLab需提前预约；不去展就逛 DiverCity/维纳斯城堡。"},
                    {"time": "18:00-20:00", "title": "海湾夜景+晚餐", "description": "日落前后最美；返回市区建议避开通勤高峰。"},
                ],
            },
        ],
        "packing": ["护照/签证材料", "Suica/PASMO（或手机交通卡）", "转换插头", "舒适步行鞋", "随身零钱/硬币包", "充电宝"],
    },
    "首尔": {
        "best_season": "4-6月 / 9-11月",
        "pace": "适中",
        "highlights": 8,
        "areas": ["景福宫", "北村韩屋村", "弘大", "明洞", "梨泰院", "东大门"],
        "days": [],
        "packing": ["护照/签证材料", "转换插头", "舒适步行鞋", "充电宝"],
    },
}

def build_realistic_mock_itinerary(start: str, dest: str, days: int, budget: str) -> dict:
    """More realistic non-AI itinerary: concrete places, time blocks, and movement."""
    budget_num = parse_budget_to_number(budget)
    dest_norm = normalize_destination(dest)
    rng = _stable_rng(start, dest_norm, str(days), budget)

    def _time_block(label: str) -> str:
        m = {
            "上午": "09:00-12:00",
            "中午": "12:00-13:30",
            "下午": "13:30-17:00",
            "傍晚": "17:30-19:30",
            "晚上": "19:30-21:30",
        }
        return m.get(label, label)

    def _enhance_activity(a: dict) -> dict:
        # keep keys compatible with frontend (time/title/description)
        time = _time_block(a.get("time", ""))
        title = a.get("title") or a.get("name") or ""
        desc = (a.get("description") or "").strip()
        # add a light, practical note to avoid generic tone
        if desc and "建议" not in desc:
            desc += "（尽量同一区域串联，地铁+步行优先，少折返）"
        # best-effort structured hints for template activities
        transport = a.get("transport") or ("地铁/步行" if "公园" in title or "胡同" in title else "地铁为主，必要时打车")
        duration = a.get("duration") or ("约 2-3 小时" if time in ("09:00-12:00", "13:30-17:00") else "约 1-2 小时")
        food = a.get("food") or []
        alternatives = a.get("alternatives") or []
        booking_tip = a.get("booking_tip") or ("热门景点建议提前 1-3 天预约/购票" if ("博物馆" in title or "故宫" in title or "长城" in title) else "")
        return {
            "time": time,
            "title": title,
            "description": desc,
            "transport": transport,
            "duration": duration,
            "food": food,
            "alternatives": alternatives,
            "booking_tip": booking_tip,
        }

    # If we have a POI pack, use it; otherwise enhance existing templates.
    pack = POI_DB.get(dest_norm)
    if pack:
        base_days = pack.get("days", [])
        daily_plan = []
        for i in range(days):
            if i < len(base_days):
                d = base_days[i]
                daily_plan.append({"day": i + 1, "title": d["title"], "activities": d["activities"]})
            else:
                # extra days: pick a relaxed structure around areas
                area = rng.choice(pack.get("areas", [dest_norm]))
                daily_plan.append({
                    "day": i + 1,
                    "title": f"{area}·自由探索与补漏",
                    "activities": [
                        {"time": "10:00-12:00", "title": f"{area}慢逛（咖啡/街区）", "description": "按兴趣补打卡；建议把购物/伴手礼放在最后几天集中处理。"},
                        {"time": "14:00-17:00", "title": "备选体验（二选一）", "description": "根据天气选择室内展馆/商场，或改为公园散步+拍照。"},
                        {"time": "18:00-20:30", "title": "当地晚餐（不赶行程）", "description": "挑离住宿近的区域，避免跨城折返；让旅行更轻松。"},
                    ],
                })

        return {
            "overview": {
                "destination": dest_norm,
                "days": days,
                "budget": budget,
                "best_season": pack.get("best_season", "春秋"),
                "pace": pack.get("pace", "适中"),
                "highlights_count": pack.get("highlights", 6),
            },
            "daily_plan": daily_plan,
            "budget_breakdown": calculate_budget_breakdown(budget_num),
            "packing_list": pack.get("packing", ["身份证/护照", "充电器", "舒适鞋子", "防晒霜"]),
            "model_info": {"model_used": "realistic_mock", "provider": "规则+POI库兜底", "note": "AI 未配置时使用更真实的行程生成"},
        }

    # If we have destination-specific templates, enhance them into more realistic blocks.
    dest_info = DESTINATION_DATA.get(dest_norm)
    if dest_info and dest_info.get("daily_plan"):
        template_days = dest_info["daily_plan"]
        daily_plan = []
        for day in range(1, days + 1):
            if day <= len(template_days):
                t = template_days[day - 1]
                acts = [_enhance_activity(a) for a in (t.get("activities") or [])]
                daily_plan.append({"day": day, "title": t.get("title", f"第{day}天"), "activities": acts})
            elif day == days:
                daily_plan.append({
                    "day": day,
                    "title": f"收尾与返程·告别{dest_norm}",
                    "activities": [
                        {"time": "09:30-11:30", "title": "轻松补漏（咖啡/伴手礼）", "description": "把没买到的伴手礼集中补齐；尽量选离住宿近的商圈。"},
                        {"time": "12:30-15:30", "title": f"返程：{dest_norm} → {start}", "description": "预留前往车站/机场的时间；重要证件与充电器最后再检查一遍。"},
                    ],
                })
            else:
                daily_plan.append({
                    "day": day,
                    "title": f"城市深挖·慢一点也很值（第{day}天）",
                    "activities": [
                        {"time": "10:00-12:00", "title": "本地生活街区散步", "description": f"避开景区主干道，去{dest_norm}更生活化的街区走走，找一家评分高的小店吃早午餐。"},
                        {"time": "14:00-17:00", "title": "小型展馆/公园二选一", "description": "按天气决定：雨天选展馆，晴天选公园/城市步道，行程更真实舒服。"},
                        {"time": "18:00-20:00", "title": "当日主题晚餐", "description": "把当地特色餐放在晚上，白天轻食更不累；注意错峰避免排队过久。"},
                    ],
                })

        return {
            "overview": {
                "destination": dest_norm,
                "days": days,
                "budget": budget,
                "best_season": dest_info.get("best_season", "春秋"),
                "pace": dest_info.get("pace", "适中"),
                "highlights_count": dest_info.get("highlights", 6),
            },
            "daily_plan": daily_plan,
            "budget_breakdown": calculate_budget_breakdown(budget_num),
            "packing_list": dest_info.get("packing", ["身份证", "充电器", "舒适鞋子", "防晒霜"]),
            "model_info": {"model_used": "realistic_template", "provider": f"{dest_norm}增强模板", "note": "AI 未配置时使用更真实的模板行程"},
        }

    # fallback to the existing generic templates
    return get_mock_data(start, dest_norm, days, budget)

def get_mock_data(start, dest, days, budget):
    """根据目的地生成定制化模拟数据，当AI模型不可用时使用"""
    budget_num = parse_budget_to_number(budget)
    
    # 查找是否有该目的地的定制数据
    dest_info = DESTINATION_DATA.get(dest)
    
    if dest_info and len(dest_info["daily_plan"]) > 0:
        daily_plan = []
        template_days = dest_info["daily_plan"]
        
        for day in range(1, days + 1):
            if day <= len(template_days):
                # 使用目的地专属行程
                template = template_days[day - 1]
                daily_plan.append({
                    "day": day,
                    "title": template["title"],
                    "activities": template["activities"]
                })
            elif day == days:
                # 最后一天：返程
                daily_plan.append({
                    "day": day,
                    "title": f"最后时光·告别{dest}",
                    "activities": [
                        {"time": "上午", "title": "自由活动", "description": f"回到{dest}最喜欢的角落，再逛一逛、拍一拍，留下最后的回忆。"},
                        {"time": "下午", "title": f"返回{start}", "description": f"收拾行李，带着满满的回忆启程返回{start}。"}
                    ]
                })
            else:
                # 中间额外天数：深度探索
                daily_plan.append({
                    "day": day,
                    "title": f"深度探索·第{day}天",
                    "activities": [
                        {"time": "上午", "title": f"{dest}隐藏景点", "description": f"避开游客热门路线，探索{dest}本地人推荐的私藏好去处。"},
                        {"time": "下午", "title": "特色手作体验", "description": f"参与{dest}当地特色的手工体验活动，制作属于自己的旅行纪念品。"},
                        {"time": "傍晚", "title": "美食探店", "description": f"打卡{dest}网红餐厅或小巷深处的大排档，发现更多美味。"}
                    ]
                })
        
        return {
            "overview": {
                "destination": dest,
                "days": days,
                "budget": budget,
                "best_season": dest_info["best_season"],
                "pace": dest_info["pace"],
                "highlights_count": dest_info["highlights"]
            },
            "daily_plan": daily_plan,
            "weather_alert": {"city": dest, "temp": "22°C", "condition": "晴朗", "warning": "紫外线较强，注意防晒"},
            "budget_breakdown": calculate_budget_breakdown(budget_num),
            "packing_list": dest_info.get("packing", ["身份证", "充电器", "舒适鞋子", "防晒霜"]),
            "model_info": {"model_used": "destination_template", "provider": f"{dest}定制模板", "note": f"已为{dest}生成专属行程方案"}
        }
    
    # 无定制数据的通用行程
    daily_plan = []
    daily_plan.append({
        "day": 1, "title": f"抵达{dest}·初探城市",
        "activities": [
            {"time": "上午", "title": f"从{start}出发前往{dest}", "description": f"建议乘坐早班交通工具，预留充足时间抵达{dest}。"},
            {"time": "下午", "title": "城市核心区漫步", "description": f"入住酒店后，在{dest}的市中心区域散步，熟悉周边环境。"},
            {"time": "傍晚", "title": "当地美食初体验", "description": f"找一家当地人推荐的餐厅，品尝{dest}的特色美食。"}
        ]
    })
    daily_plan.append({
        "day": 2, "title": "经典景点打卡",
        "activities": [
            {"time": "上午", "title": f"{dest}标志性景点", "description": f"游览{dest}最著名的景点，建议提前在线购票。"},
            {"time": "下午", "title": "文化体验", "description": f"参观{dest}的博物馆或文化街区，了解当地历史文化。"},
            {"time": "傍晚", "title": "夜景观赏", "description": f"在{dest}的最佳观景点欣赏夜景。"}
        ]
    })
    for day in range(3, days + 1):
        if day == days:
            daily_plan.append({"day": day, "title": f"告别{dest}", "activities": [{"time": "上午", "title": "最后游览", "description": f"再逛逛{dest}喜欢的角落。"}, {"time": "下午", "title": f"返回{start}", "description": f"收拾行李，带着回忆返回{start}。"}]})
        else:
            daily_plan.append({"day": day, "title": f"深度探索第{day}天", "activities": [{"time": "上午", "title": f"{dest}周边景点", "description": f"探索{dest}周边的自然风光或特色小镇。"}, {"time": "下午", "title": "自由活动", "description": "根据个人兴趣自由安排，购物、美食或休息。"}]})
    
    return {
        "overview": {"destination": dest, "days": days, "budget": budget, "best_season": "春秋", "pace": "适中", "highlights_count": 6},
        "daily_plan": daily_plan,
        "weather_alert": {"city": dest, "temp": "22°C", "condition": "晴朗", "warning": "天气适宜出行。"},
        "budget_breakdown": calculate_budget_breakdown(budget_num),
        "packing_list": ["身份证", "充电器", "舒适鞋子", "防晒霜", "常用药品"],
        "model_info": {"model_used": "generic_template", "provider": "通用模板", "note": "DeepSeek API调用失败，使用通用行程模板。配置API Key可获取AI定制行程。"}
    }
    
    return {
        "overview": {
            "destination": dest,
            "days": days,
            "budget": budget,
            "best_season": "春秋",
            "pace": "适中",
            "highlights_count": 6
        },
        "daily_plan": daily_plan,
        "weather_alert": {
            "city": dest,
            "temp": "22°C",
            "condition": "晴朗",
            "warning": "紫外线较强，注意防晒"
        },
        "budget_breakdown": calculate_budget_breakdown(budget_num),
        "packing_list": ["护照/签证", "充电器", "相机", "舒适鞋子", "防晒霜"],
        "model_info": {
            "model_used": "mock_data",
            "provider": "模拟数据",
            "note": "DeepSeek API调用失败，使用模拟数据"
        }
    }

def parse_budget_to_number(budget_str: str) -> int:
    """解析预算字符串为数字（用于计算）"""
    numbers = re.findall(r'\d+', budget_str.replace(',', ''))
    if len(numbers) >= 2:
        return (int(numbers[0]) + int(numbers[1])) // 2
    elif len(numbers) == 1:
        return int(numbers[0])
    return 5000

def calculate_budget_breakdown(total_budget: int) -> list:
    """根据总预算计算各项分配"""
    if total_budget <= 0:
        total_budget = 5000
    
    return [
        {"category": "机票/交通", "amount": int(total_budget * 0.35)},
        {"category": "酒店住宿", "amount": int(total_budget * 0.30)},
        {"category": "美食餐饮", "amount": int(total_budget * 0.20)},
        {"category": "门票娱乐", "amount": int(total_budget * 0.15)}
    ]

@app.get("/")
async def root():
    return {"message": "VoyageAI API 服务运行中"}

@app.get("/api/health")
async def health_check():
    """健康检查接口"""
    return {
        "status": "healthy",
        "service": "VoyageAI Travel Planner",
        "ai_provider": "DeepSeek",
        "weather_service": "OpenWeatherMap" if settings.openweather_api_key else "Disabled",
        "cache_enabled": True
    }

@app.get("/api/config")
async def get_config():
    """获取当前配置信息"""
    return {
        "ai_provider": "DeepSeek",
        "model": DEEPSEEK_MODEL,
        "weather_enabled": bool(settings.openweather_api_key and settings.openweather_api_key != "eaad9d3c97b90d588cffb2835dc80129"),
        "cache_enabled": True,
        "deepseek_key_set": bool(settings.deepseek_api_key and settings.deepseek_api_key != "your_deepseek_api_key_here")
    }

@app.get("/api/weather")
async def get_weather(city: str):
    """获取指定城市的天气数据"""
    logger.info(f"获取{city}的天气数据")
    weather_data = await get_weather_data(city)
    return weather_data

from pydantic import BaseModel, Field

class PlanRequest(BaseModel):
    start: str = Field(..., description="出发地")
    dest: str = Field(..., description="目的地")
    days: int = Field(..., ge=1, le=30, description="游玩天数")
    budget: str = Field(..., description="预算范围")

@app.post("/api/plan")
async def plan(request: PlanRequest, db: Session = Depends(get_db)):
    """生成旅行规划"""
    try:
        start = request.start.strip()
        dest = request.dest.strip()
        days = request.days
        budget = request.budget.strip()
        
        # 输入验证
        errors = []
        if not start:
            errors.append("出发地不能为空")
        if not dest:
            errors.append("目的地不能为空")
        if not budget:
            errors.append("预算不能为空")
        elif not re.match(r'^\d+(-\d+)?(\+)?$', budget.replace(',', '')):
            errors.append("预算格式不正确，示例：5000-8000 或 10000+")
        
        if errors:
            raise HTTPException(status_code=400, detail={"error": "输入验证失败", "details": errors})
        
        # 并行执行：同时调用 AI 和天气 API
        itinerary_task = generate_itinerary(start, dest, days, budget)
        weather_task = get_weather_data(dest)
        
        itinerary, weather_data = await asyncio.gather(itinerary_task, weather_task)
        
        if weather_data:
            itinerary["weather_alert"] = weather_data
        
        # 保存行程到数据库
        try:
            db_itinerary = Itinerary(
                start_location=start,
                destination=dest,
                days=days,
                budget=budget,
                overview=json.dumps(itinerary.get("overview", {})),
                daily_plan=json.dumps(itinerary.get("daily_plan", [])),
                budget_breakdown=json.dumps(itinerary.get("budget_breakdown", [])),
                packing_list=json.dumps(itinerary.get("packing_list", [])),
                weather_alert=json.dumps(itinerary.get("weather_alert", {})),
                model_info=json.dumps(itinerary.get("model_info", {}))
            )
            db.add(db_itinerary)
            db.commit()
            db.refresh(db_itinerary)
            itinerary["id"] = db_itinerary.id
        except Exception as db_error:
            print(f"数据库保存失败：{db_error}")
            # 数据库保存失败不影响返回结果
        
        return itinerary
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"行程规划异常：{e}")
        raise HTTPException(status_code=500, detail={"error": "服务器内部错误", "details": str(e)})

# 全局异常处理器
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """全局异常处理器"""
    logger.error(f"全局异常: {exc}")
    logger.error(traceback.format_exc())
    
    # 根据异常类型返回不同的错误信息
    if isinstance(exc, HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content=exc.detail
        )
    elif isinstance(exc, (APIError, APIConnectionError, RateLimitError)):
        return JSONResponse(
            status_code=503,
            content={
                "error": "AI服务异常",
                "details": "AI服务暂时不可用，请稍后重试",
                "error_type": type(exc).__name__
            }
        )
    elif isinstance(exc, SQLAlchemyError):
        return JSONResponse(
            status_code=500,
            content={
                "error": "数据库异常",
                "details": "数据库操作失败，请稍后重试",
                "error_type": "DatabaseError"
            }
        )
    elif isinstance(exc, httpx.HTTPError):
        return JSONResponse(
            status_code=503,
            content={
                "error": "外部服务异常",
                "details": "天气服务暂时不可用",
                "error_type": "ExternalServiceError"
            }
        )
    else:
        return JSONResponse(
            status_code=500,
            content={
                "error": "服务器内部错误",
                "details": "系统遇到未知错误，请稍后重试",
                "error_type": type(exc).__name__
            }
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
