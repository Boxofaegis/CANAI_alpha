import requests
import json
from app import *
def CAN_weather_sr(city):

    apiKey = '6420fce40f49219f6973ef24be638fc7'
    lang = 'kr' #언어
    units = 'metric' #화씨 온도를 섭씨 온도로 변경
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"

    result = requests.get(api)
    result = json.loads(result.text)

    name = result['name']
    lon = result['coord']['lon']
    lat = result['coord']['lat']
    weather = result['weather'][0]['main']
    temperature = result['main']['temp']
    humidity = result['main']['humidity']

    print(name)
    print(lon, ', ', lat)
    print(weather)
    print(temperature)
    print(humidity)