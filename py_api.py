import requests
import json

# Get a key from openWeatherAPI 
APP_KEY = '1e29315832bb4aee6521a66797caaf50'
# Set latitude and longitude
lat = "35.6952901"
lng = "-0.6393881" 
def get_data(lat, lng):
    # get data
    url = 'http://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&appid=1e29315832bb4aee6521a66797caaf50'.format(lat, lng)
    data = requests.get(url)
    # Parse data from String to Python Dictionnary
    return json.loads(data.content)

# Parse Kelvin temperature to Celsius
def kelvin_to_celsius(temp):
    return temp-274.15

# Get data from server
weather = get_data(lat, lng)
temprature = kelvin_to_celsius(weather['main']['temp'])
# Save tempurature to use it in other *.py files
def temp():
    return temprature