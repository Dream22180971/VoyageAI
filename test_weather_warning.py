import httpx
import json

def get_city_adcode(city, api_key):
    """获取城市的adcode"""
    url = f"https://restapi.amap.com/v3/geocode/geo?address={city}&key={api_key}"
    response = httpx.get(url, timeout=10.0)
    if response.status_code == 200:
        data = response.json()
        if data.get("status") == "1" and data.get("geocodes"):
            return data["geocodes"][0]["adcode"]
    return None

def get_weather_data(city, api_key):
    """获取天气数据"""
    adcode = get_city_adcode(city, api_key)
    if not adcode:
        return None
    
    url = f"https://restapi.amap.com/v3/weather/weatherInfo?city={adcode}&key={api_key}"
    response = httpx.get(url, timeout=10.0)
    if response.status_code == 200:
        data = response.json()
        if data.get("status") == "1" and data.get("lives"):
            return data["lives"][0]
    return None

def get_weather_warning(weather_data):
    """根据天气数据生成预警提示（适配高德地图数据格式）"""
    warnings = []
    
    # 从高德地图数据中提取信息
    temp = float(weather_data.get("temperature", 22))
    humidity = int(weather_data.get("humidity", 50))
    weather_desc = weather_data.get("weather", "").lower()
    wind_power = weather_data.get("windpower", "≤3")
    
    print(f"天气数据:")
    print(f"  温度: {temp}°C")
    print(f"  湿度: {humidity}%")
    print(f"  天气状况: {weather_desc}")
    print(f"  风力: {wind_power}")
    
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

def test_weather_warning():
    """测试天气预警功能"""
    
    # 高德地图API密钥
    api_key = "be65ac450aa1d2ace7afb3d3640594ba"
    
    # 测试城市列表
    test_cities = ["北京", "上海", "广州", "深圳", "南京"]
    
    print("测试天气预警功能")
    print("=" * 60)
    
    for city in test_cities:
        print(f"\n城市: {city}")
        print("-" * 30)
        
        # 获取天气数据
        weather_data = get_weather_data(city, api_key)
        
        if weather_data:
            # 生成预警
            warning = get_weather_warning(weather_data)
            print(f"预警信息: {warning}")
        else:
            print(f"❌ 无法获取{city}的天气数据")

if __name__ == "__main__":
    test_weather_warning()