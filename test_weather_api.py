import httpx
import json
import time

def test_weather_api():
    """测试OpenWeatherMap API密钥是否能正常连接"""
    
    # 默认API密钥
    api_key = "eaad9d3c97b90d588cffb2835dc80129"
    
    # 测试城市：江苏南京
    city = "Nanjing"
    
    # API URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=zh_cn"
    
    print(f"正在测试OpenWeatherMap API连接...")
    print(f"API密钥: {api_key}")
    print(f"测试城市: {city}")
    print(f"API URL: {url}")
    print("-" * 60)
    
    max_retries = 3
    
    for retry in range(max_retries):
        print(f"\n尝试 {retry + 1}/{max_retries}...")
        
        try:
            # 创建客户端配置
            client = httpx.Client(
                timeout=20.0,
                follow_redirects=True,
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                }
            )
            
            # 发送请求
            response = client.get(url)
            
            print(f"HTTP状态码: {response.status_code}")
            
            if response.status_code == 200:
                # 解析JSON数据
                data = response.json()
                
                # 提取关键信息
                city_name = data.get("name", "未知城市")
                temp = data["main"]["temp"]
                temp_min = data["main"]["temp_min"]
                temp_max = data["main"]["temp_max"]
                condition = data["weather"][0]["description"]
                humidity = data["main"]["humidity"]
                feels_like = data["main"]["feels_like"]
                
                print(f"✅ API连接成功！")
                print(f"城市: {city_name}")
                print(f"当前温度: {int(temp)}°C")
                print(f"最低温度: {int(temp_min)}°C")
                print(f"最高温度: {int(temp_max)}°C")
                print(f"天气状况: {condition}")
                print(f"湿度: {humidity}%")
                print(f"体感温度: {int(feels_like)}°C")
                
                # 保存完整响应到文件
                with open("weather_api_response.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"\n完整响应已保存到: weather_api_response.json")
                
                return True
                
            elif response.status_code == 401:
                print(f"❌ API密钥无效或过期")
                print(f"错误信息: {response.text[:200]}...")
                return False
                
            elif response.status_code == 404:
                print(f"❌ 城市未找到")
                print(f"错误信息: {response.text[:200]}...")
                return False
                
            else:
                print(f"❌ API请求失败")
                print(f"错误信息: {response.text[:200]}...")
                if retry < max_retries - 1:
                    print(f"等待2秒后重试...")
                    time.sleep(2)
                    continue
                return False
                
        except httpx.ConnectTimeout:
            print(f"❌ 网络连接超时")
            
        except httpx.ConnectError:
            print(f"❌ 网络连接错误")
            
        except httpx.ReadTimeout:
            print(f"❌ 读取超时")
            
        except httpx.HTTPError as e:
            print(f"❌ HTTP错误: {e}")
            
        except Exception as e:
            print(f"❌ 未知错误: {e}")
            
        if retry < max_retries - 1:
            print(f"等待2秒后重试...")
            time.sleep(2)
    
    print("\n所有重试都失败了")
    return False

def test_network_connectivity():
    """测试网络连接性"""
    print("\n测试网络连接性...")
    
    test_urls = [
        "https://google.com",
        "https://api.openweathermap.org",
        "https://www.baidu.com"
    ]
    
    for url in test_urls:
        try:
            response = httpx.get(url, timeout=10.0)
            print(f"✅ {url} 连接成功 (状态码: {response.status_code})")
        except Exception as e:
            print(f"❌ {url} 连接失败: {e}")

if __name__ == "__main__":
    # 先测试网络连接性
    test_network_connectivity()
    
    # 再测试天气API
    success = test_weather_api()
    
    if success:
        print("\n🎉 测试成功！API密钥可以正常使用")
    else:
        print("\n❌ 测试失败！API密钥无法正常使用")
        print("\n可能的原因：")
        print("1. 网络连接问题")
        print("2. API密钥无效或过期")
        print("3. OpenWeatherMap服务器问题")
        print("4. 防火墙或代理限制")