# -*- encoding:utf-8 -*-

__date__ = '2018/12/28/028 15:53'

import requests


def get_weather(area):
    result = requests.get(
        url="http://api.map.baidu.com/telematics/v3/weather",
        params={
            "location": area[2:],
            "output": "json",
            "ak": "2ab217b314342871ed183dddf165df75",
        }
    ).json()
    if result.get("status", "") == "success":
        weather = result.get("results", "")[0]
        res = weather_parse(weather)
        return res
    return "未查询到天气情况。"


def weather_parse(weather):
    city = weather.get("currentCity", "")
    pm25 = weather.get("pm25", "")
    weather_data = weather.get("weather_data", "")[0]
    weather = weather_data.get("weather", "")
    temperature = weather_data.get("temperature", "")
    wind = weather_data.get("wind", "")
    return "城市：{0}\n PM25：{1}\n 天气：{2}\n 气温：{3}\n 风力：{4}".format(
        city, pm25, weather, temperature, wind
    )
