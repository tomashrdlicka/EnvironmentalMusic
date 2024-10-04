import time
import requests
import geocoder

from pythonosc import osc_message_builder
from pythonosc import udp_client


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius


if __name__ == "__main__":

    isConnected = True

    # Geolocation data
    g = geocoder.ip('me')
    BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?"
    BASE_URL_GEO = "http://api.openweathermap.org/geo/1.0/reverse?"
    # Replace YYY with an API key from https://openweathermap.org/api
    API_KEY = "188e5209e69ed503e767cb89d4104265"
    CITY = str(g.city)
    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

    # Replace XXXXX with computer's current IP address
    client = udp_client.SimpleUDPClient("192.168.1.111", 7000)

    while (isConnected):

        response = requests.get(url).json()
        temp_now = kelvin_to_celsius(response['list'][1]['main']['temp'])
        temp_feelsLike = kelvin_to_celsius(response['list'][1]['main']['feels_like'])
        pressure = response['list'][1]['main']['pressure']

        temperatureOffset = round(abs(temp_now - temp_feelsLike), 0)
        temperatureOffset = int(str(temperatureOffset)[0:1])
        temperatureSelector = round(temp_feelsLike, 0)
        pressureSelector = int(str(pressure)[2:3])

        client.send_message("/temperatureFeels", temperatureSelector)
        client.send_message("/pressure", pressureSelector)
        client.send_message("/temperatureOffset", temperatureOffset)

        time.sleep(10)
