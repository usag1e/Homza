from pprint import pprint
import requests
import datetime
import time

# Function to get the weather in Montreal
def getWeather():
	status= {}
	# Requesting weather from OpenWeatherMap for Montreal, in .json
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&mode=json&units=metric&APPID=b55dc015063b76e0ba8531ffa35d7df6' % ( 45.50, -73.56 ) )
    #extracting the .json data from the request
	print r
	rj = r.json()
    # Printing the whole .json thing, with pprint() 'cause they say it's nicer
    #print rj
	#pprint(rj)
    # Temperature is called 'temp' and indented in 'main', we retrieve it
	pressure = rj['main']['pressure']
	temperature = rj['main']['temp']
        icon = rj['weather'][0]['icon']
	state = rj['weather'][0]['description']
	ID = rj['weather'][0]['id']
	SR = rj['sys']['sunrise']
	SS = rj['sys']['sunset']
	wind = rj['wind']['speed']

	sunrise = (
    datetime.datetime.fromtimestamp(
        int(SR)
    ).strftime('%Y-%m-%d %H:%M:%S')
)
	sunset = (
    datetime.datetime.fromtimestamp(
        int(SS)
    ).strftime('%Y-%m-%d %H:%M:%S')
)
	time_of_treatment = (
    datetime.datetime.fromtimestamp(
        int(time.mktime(time.localtime()))
    ).strftime('%Y-%m-%d %H:%M:%S')
)
	print time_of_treatment

	status['temperature'] = temperature
	status['pressure'] = pressure
	status['state'] = state
	status['ID'] = ID
	status['sunrise'] = sunrise
	status['sunset'] = sunset
	status['wind'] = wind
	status['time'] = time_of_treatment
        status['icon'] = icon


	print '[Weather] The temperature is:', temperature ,'C'
	print '[Weather] The pressure is:', pressure
	print '[Weather] The current state is:', state
	return status


