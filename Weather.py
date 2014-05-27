from pprint import pprint
import requests
import RPi.GPIO as GPIO
import time
from DBhandler import getHomeFromDB, insertWeather, getTemperatureFromDB

# Function to get the weather in Montreal
def getWeather() :
    home = getHomeFromDB()
    # Requesting weather from OpenWeatherMap for Montreal, in .json
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&mode=json&units=metric' % ( home.lat, home.lon ) )
    #extracting the .json data from the request
    rj = r.json()
    # Printing the whole .json thing, with pprint() 'cause they say it's nicer
    # pprint(rj)
    # Temperature is called 'temp' and indented in 'main', we retrieve it
    temperature = rj['main']['temp']
    print '[Weather] The temperature is:', temperature
    insertWeather( rj[ 'id' ], rj[ 'name' ], rj[ 'clouds' ][ 'all' ], rj[ 'dt' ], rj[ 'main' ][ 'humidity' ], rj[ 'main' ][ 'pressure' ], rj[ 'main' ][ 'temp' ], rj[ 'main' ][ 'temp_max' ], rj[ 'main' ][ 'temp_min' ], rj[ 'rain' ][ '3h' ], rj[ 'sys' ][ 'sunrise' ], rj[ 'sys' ][ 'sunset' ], rj[ 'weather' ][0][ 'main' ], rj[ 'weather' ][0][ 'description' ], rj[ 'weather' ][0][ 'icon' ], rj[ 'wind' ][ 'deg' ], rj[ 'wind' ][ 'speed' ] ) 

def displayWeather( X ) :
    temperature = getTemperatureFromDB()
    if temperature > 18 :
       	GPIO.output( X, True )
       	print( '[Weather] Temperature is more than 18 degrees - %d is ON' % X )
    else:
       	GPIO.output( X, False )
       	print( '[Weather] Temperature is below 18 degrees - %d is OFF' % X )
