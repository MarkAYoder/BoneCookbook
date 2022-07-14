#!/usr/bin/env python3
# Displays current weather and forcast
import os
import sys
from datetime import datetime
import requests     # For getting weather
                
# http://api.openweathermap.org/data/2.5/onecall
params = {
    'appid': os.environ['APPID'],
    # 'city': 'brazil,indiana',
    'exclude': "minutely,hourly",
    'lat':  '39.52',
    'lon': '-87.12',
    'units': 'imperial'
    }
urlWeather = "http://api.openweathermap.org/data/2.5/onecall"

print("Getting weather")

try:
    r = requests.get(urlWeather, params=params)
    if(r.status_code==200):
        # print("headers: ", r.headers)
        # print("text: ", r.text)
        # print("json: ", r.json())
        weather = r.json()
        print("Temp: ", weather['current']['temp'])         # <1>
        print("Humid:", weather['current']['humidity'])
        print("Low:  ", weather['daily'][1]['temp']['min'])
        print("High: ", weather['daily'][0]['temp']['max'])
        day = weather['daily'][0]['sunrise']-weather['timezone_offset']
        print("sunrise: " + datetime.utcfromtimestamp(day).strftime('%Y-%m-%d %H:%M:%S'))
        # print("Day: " + datetime.utcfromtimestamp(day).strftime('%a'))
        # print("weather: ", weather['daily'][1])           # <2>
        # print("weather: ", weather)                       # <3>
        # print("icon: ", weather['current']['weather'][0]['icon'])
        # print()

    else:
        print("status_code: ", r.status_code)
except IOError:
    print("File not found: " + tmp101)
    print("Have you run setup.sh?")
except:
    print("Unexpected error:", sys.exc_info())
