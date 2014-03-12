from pprint import pprint
import requests

#Requesting weather from OpenWeatherMap for Montreal, in .json
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Montreal&mode=json&units=metric')
#extracting the .json data from the request
rj = r.json()
#Printing the whole .json thing, with pprint() 'cause they say it's nicer
pprint(rj)

#Temperature is called 'temp' and indented in 'main', we retrieve it
temperature = rj['main']['temp']
print('The temperature in Montreal is:', temperature)
description = rj['weather'][0]['description']
print('The weather is', description)



