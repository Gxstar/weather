import requests

def get_weather(location):
    location='116.41,39.92'
    key='a4fd577d6ece4f00957cc757874c2787'
    url="https://devapi.qweather.com/v7/weather/now?location="+location+"&key="+key
    result=requests.get(url)
    return result