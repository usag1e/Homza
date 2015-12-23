# -*- coding: utf-8 -*-
from house import House
from internet import Internet
import logging
import calendar, time
from entity import Entity

logger = logging.getLogger(__name__)

class IssFinder(Entity):
    _collection = 'homza'
    _type = 'iss'
    
    def __init__(self):
        self._id = "iss"
        self.next_passage()
        self.create()
        
    def next_passage(self):
        house = House()
        if not house.latitude and not house.longitude:
            print "IN IF"
            logger.error("Could not find latitude or longitude.")
            return False
        # Requesting ISS from Open-notify.org for Montreal, in .json
        request_url = 'http://api.open-notify.org/iss-pass.json?lat=%s&lon=%s' % ( house.latitude, house.longitude )      
        print request_url  
        response = Internet.get(request_url)
        print response
        object_response = response.json()
        if object_response:
            self.date = object_response['response'][0]['risetime']
            self.duration = object_response['response'][0]['duration']
            self.remaining = object_response['response'][0][ 'risetime' ] - calendar.timegm(time.gmtime())
            
            
