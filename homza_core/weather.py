# -*- coding: utf-8 -*-
from house import House
from internet import Internet
import logging
import requests
import datetime
import time
from entity import Entity

logger = logging.getLogger(__name__)

class WeatherCenter(Entity):
    _collection = 'homza'
    _type = 'weather'

    def __init__(self):
        self._id = "weather"
        self.type = WeatherCenter._type
        self.getWeather()
        self.update()
        logger.info("Updated Weather data.")
        logger.info(" %s C" % self.temperature)
        logger.info("%s" % self.state)
        
    def __call__(self):
        self.__init__()
           
    def getWeather(self):
        house = House()
        status= {}
        # Requesting weather from OpenWeatherMap for Montreal, in .json
        try:
            r = Internet.get('http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&mode=json&units=metric&APPID=b55dc015063b76e0ba8531ffa35d7df6' % ( house.latitude, house.longitude ) )
            #extracting the .json data from the request
            rj = r.json()
            
            if rj:
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
                	    ).strftime('%Y%m%d%H%M%S')
	            )
                sunset = (
	                datetime.datetime.fromtimestamp(
		            int(SS)
	                ).strftime('%Y%m%d%H%M%S')
	            )
                time_of_treatment = (
	                datetime.datetime.fromtimestamp(
		            int(time.mktime(time.localtime()))
	                ).strftime('%Y%m%d%H%M%S')
	            )
                self.time = time_of_treatment
                self.wind = wind
                self.sunset = sunset
                self.sunrise = sunrise
                self.ID = ID
                self.state = state
                self.pressure = pressure
                self.temperature = temperature
                self.icon = icon
        except:
            pass
