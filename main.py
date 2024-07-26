import requests
from win10toast import ToastNotifier
from dotenv import load_dotenv
import os 

load_dotenv()

API_KEY = os.getenv('KEY')
CITY = input("Enter the city you are in: ")
BASE_URL = f"https://api.openweathermap.org/data/2.5/weather?"

url = BASE_URL +  "appid=" + API_KEY + "&q=" + CITY
n = ToastNotifier()
def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius
response = requests.get(url).json()
# print(response)
temp_kelvin = response["main"]["temp"]
temp_celsius = round(kelvin_to_celsius(temp_kelvin),1)
feels_like_kelvin = response["main"]["feels_like"]
feels_like_celsius = round(kelvin_to_celsius(feels_like_kelvin),1)
humidity = response["main"]["humidity"]
description = response["weather"][0]["description"]


result = f"Current temperature:{temp_celsius}°C" + "\n" + f"Feels like: {feels_like_celsius}°C" + "\n" + f"Humidity: {humidity}%"
n.show_toast("Weather update", result, duration = 10)
