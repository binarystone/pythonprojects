#!/usr/bin/env python3

import requests

def get_weather(city):
    api_key = 'YOUR_API_KEY'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    return weather_data

def display_weather(weather_data):
    if weather_data['cod'] == '404':
        print('City not found.')
    else:
        city_name = weather_data['name']
        weather_desc = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        print(f'Weather in {city_name}:')
        print(f'Description: {weather_desc}')
        print(f'Temperature: {temp}°C')
        print(f'Humidity: {humidity}%')

city = input('Enter city name: ')
weather_data = get_weather(city)
display_weather(weather_data)
