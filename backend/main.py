import os
import json
import httpx
import re
import asyncio
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
deepseek_client = OpenAI(
    api_key=settings.deepseek_api_key,
    base_url="https://api.deepseek.com/v1"
)

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
          "time": "时间段",
          "title": "活动名称",
          "description": "详细描述（请根据预算{budget}推荐合适的消费场所和活动）",
          "icon": "solar:xxx"
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
        return get_mock_data(start, dest, days, budget)

def get_mock_data(start, dest, days, budget):
    """临时模拟数据，当模型不可用时使用"""
    budget_num = parse_budget_to_number(budget)
    
    # 生成对应天数的行程
    daily_plan = []
    
    # 第1天：抵达和初探
    daily_plan.append({
        "day": 1,
        "title": f"抵达{dest}，初探城市风貌",
        "activities": [
            {"time": "上午", "title": f"从{start}出发", "description": f"建议乘坐早班航班前往{dest}。", "icon": "solar:plain-2-bold"},
            {"time": "下午", "title": "城市观光", "description": "游览标志性景点，品尝当地美食。", "icon": "solar:chef-hat-heart-bold"},
            {"time": "傍晚", "title": "海滨落日", "description": "在最佳观景点欣赏日落。", "icon": "solar:sunset-bold"}
        ]
    })
    
    # 第2天：文化体验
    daily_plan.append({
        "day": 2,
        "title": "文化深度体验",
        "activities": [
            {"time": "上午", "title": "历史遗迹", "description": "参观著名古迹。", "icon": "solar:castle-bold"},
            {"time": "下午", "title": "传统手工艺体验", "description": "参与当地手作工坊。", "icon": "solar:palette-bold"}
        ]
    })
    
    # 第3天及以后的行程
    for day in range(3, days + 1):
        if day == 3:
            daily_plan.append({
                "day": day,
                "title": "自然风光探索",
                "activities": [
                    {"time": "上午", "title": "郊外徒步", "description": "探索周边自然景观。", "icon": "solar:hiking-bold"},
                    {"time": "下午", "title": "特色体验", "description": "参与当地特色活动。", "icon": "solar:flag-bold"}
                ]
            })
        elif day == 4:
            daily_plan.append({
                "day": day,
                "title": "休闲放松日",
                "activities": [
                    {"time": "上午", "title": "自由活动", "description": "根据个人兴趣安排。", "icon": "solar:sun-bold"},
                    {"time": "下午", "title": "购物体验", "description": "购买当地特色纪念品。", "icon": "solar:shopping-bag-bold"}
                ]
            })
        elif day == 5:
            daily_plan.append({
                "day": day,
                "title": "告别之旅",
                "activities": [
                    {"time": "上午", "title": "最后游览", "description": "再次游览喜欢的景点。", "icon": "solar:map-point-bold"},
                    {"time": "下午", "title": "返程准备", "description": "收拾行李，准备返回。", "icon": "solar:briefcase-bold"}
                ]
            })
        else:  # 超过5天的情况
            daily_plan.append({
                "day": day,
                "title": f"深度探索第{day-2}天",
                "activities": [
                    {"time": "上午", "title": "特色景点", "description": "游览当地特色景点。", "icon": "solar:mountain-bold"},
                    {"time": "下午", "title": "美食探索", "description": "品尝更多当地美食。", "icon": "solar:fork-knife-bold"}
                ]
            })
    
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
    uvicorn.run(app, host="0.0.0.0", port=8000)
