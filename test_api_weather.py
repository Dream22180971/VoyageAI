import httpx
import json

def test_weather_api_endpoint():
    """测试后端天气API端点"""
    
    # API端点
    api_url = "http://localhost:8000/api/weather"
    
    # 测试城市列表
    test_cities = ["北京", "上海", "广州", "深圳", "南京"]
    
    print("测试后端天气API端点")
    print("=" * 60)
    
    for city in test_cities:
        print(f"\n城市: {city}")
        print("-" * 30)
        
        try:
            # 调用天气API
            url = f"{api_url}?city={city}"
            response = httpx.get(url, timeout=10.0)
            
            print(f"HTTP状态码: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                print(f"响应数据: {json.dumps(data, indent=2, ensure_ascii=False)}")
                
                # 检查返回的数据格式
                if "temp" in data and "condition" in data:
                    print(f"✅ 天气数据获取成功！")
                    print(f"  温度: {data['temp']}")
                    print(f"  天气状况: {data['condition']}")
                    if "warning" in data:
                        print(f"  预警信息: {data['warning']}")
                else:
                    print(f"❌ 天气数据格式不正确")
                    
            else:
                print(f"❌ API请求失败: {response.status_code}")
                print(f"错误信息: {response.text}")
                
        except httpx.TimeoutException:
            print(f"❌ 网络连接超时")
        except httpx.HTTPError as e:
            print(f"❌ HTTP错误: {e}")
        except Exception as e:
            print(f"❌ 未知错误: {e}")

if __name__ == "__main__":
    test_weather_api_endpoint()