import httpx
import json

def test_amap_weather_api():
    """测试高德地图天气API连接"""
    
    # 高德地图API密钥
    api_key = "be65ac450aa1d2ace7afb3d3640594ba"
    
    # 测试城市：江苏南京
    city = "南京"
    
    print(f"正在测试高德地图天气API连接...")
    print(f"API密钥: {api_key}")
    print(f"测试城市: {city}")
    print("-" * 60)
    
    # 第一步：获取城市adcode
    try:
        geocode_url = f"https://restapi.amap.com/v3/geocode/geo?address={city}&key={api_key}"
        print(f"\n1. 获取城市adcode...")
        print(f"请求URL: {geocode_url}")
        
        response = httpx.get(geocode_url, timeout=10.0)
        print(f"HTTP状态码: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"响应数据: {json.dumps(data, indent=2, ensure_ascii=False)}")
            
            if data.get("status") == "1" and data.get("geocodes"):
                adcode = data["geocodes"][0]["adcode"]
                print(f"✅ 成功获取{city}的adcode: {adcode}")
                
                # 第二步：获取天气数据
                weather_url = f"https://restapi.amap.com/v3/weather/weatherInfo?city={adcode}&key={api_key}"
                print(f"\n2. 获取天气数据...")
                print(f"请求URL: {weather_url}")
                
                weather_response = httpx.get(weather_url, timeout=10.0)
                print(f"HTTP状态码: {weather_response.status_code}")
                
                if weather_response.status_code == 200:
                    weather_data = weather_response.json()
                    print(f"响应数据: {json.dumps(weather_data, indent=2, ensure_ascii=False)}")
                    
                    if weather_data.get("status") == "1" and weather_data.get("lives"):
                        live_data = weather_data["lives"][0]
                        print(f"\n✅ 天气数据获取成功！")
                        print(f"城市: {live_data.get('city', '未知')}")
                        print(f"温度: {live_data['temperature']}°C")
                        print(f"天气状况: {live_data['weather']}")
                        print(f"湿度: {live_data.get('humidity', 'N/A')}%")
                        print(f"风向: {live_data.get('winddirection', 'N/A')}")
                        print(f"风力: {live_data.get('windpower', 'N/A')}")
                        print(f"更新时间: {live_data.get('reporttime', 'N/A')}")
                        
                        # 保存完整响应到文件
                        with open("amap_weather_response.json", "w", encoding="utf-8") as f:
                            json.dump(weather_data, f, indent=2, ensure_ascii=False)
                        print(f"\n完整响应已保存到: amap_weather_response.json")
                        
                        return True
                    else:
                        print(f"❌ 天气数据解析失败")
                        return False
                else:
                    print(f"❌ 天气API请求失败")
                    return False
            else:
                print(f"❌ 获取城市adcode失败")
                return False
        else:
            print(f"❌ 地理编码API请求失败")
            return False
            
    except httpx.TimeoutException:
        print(f"❌ 网络连接超时")
        return False
    except httpx.HTTPError as e:
        print(f"❌ HTTP错误: {e}")
        return False
    except Exception as e:
        print(f"❌ 未知错误: {e}")
        return False

def test_network_connectivity():
    """测试网络连接性"""
    print("\n测试网络连接性...")
    
    test_urls = [
        "https://restapi.amap.com",
        "https://www.amap.com",
        "https://www.baidu.com"
    ]
    
    for url in test_urls:
        try:
            response = httpx.get(url, timeout=5.0)
            print(f"✅ {url} 连接成功 (状态码: {response.status_code})")
        except Exception as e:
            print(f"❌ {url} 连接失败: {e}")

if __name__ == "__main__":
    # 先测试网络连接性
    test_network_connectivity()
    
    # 再测试高德地图天气API
    success = test_amap_weather_api()
    
    if success:
        print("\n🎉 测试成功！高德地图天气API可以正常使用")
    else:
        print("\n❌ 测试失败！高德地图天气API无法正常使用")
        print("\n可能的原因：")
        print("1. 网络连接问题")
        print("2. API密钥无效或过期")
        print("3. 高德地图服务器问题")
        print("4. 城市名称格式不正确")