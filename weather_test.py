from pprint import pprint
import requests


# Function to get the weather in Montreal
def getWeather() :
    # Requesting weather from OpenWeatherMap for Montreal, in .json
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&mode=json&units=metric' % ( 45.49266, -73.62500 ) )
    #extracting the .json data from the request
    rj = r.json()
    # Printing the whole .json thing, with pprint() 'cause they say it's nicer
    #print rj
    #pprint(rj)
    # Temperature is called 'temp' and indented in 'main', we retrieve it
    pressure = rj['main']['pressure']
    temperature = rj['main']['temp']
    print '[Weather] The temperature is:', temperature ,'C'
    print '[Weather] The pressure is:', pressure
    return temperature



