# -*- coding: utf-8 -*-
from house import House
from internet import Internet
import logging
import calendar, time
from entity import Entity
from alttime import AltTime

logger = logging.getLogger(__name__)

class IssFinder(Entity):
    _collection = 'homza'
    _type = 'iss'
    
    def __init__(self):
        self._id = "iss"
        self.type = IssFinder._type
        self.next_passage()
        self.update()
        logger.info("Updated Iss data.")
        logger.info("Next passage is %s" % self.date)
        
    def __call__(self):
        self.__init__()
        
    def next_passage(self):
        house = House()
        if not house.latitude and not house.longitude:
            logger.error("Could not find latitude or longitude.")
            return False
        # Requesting ISS from Open-notify.org for Montreal, in .json
        request_url = 'http://api.open-notify.org/iss-pass.json?lat=%s&lon=%s' % ( house.latitude, house.longitude )      
        response = Internet.get(request_url)
        object_response = response.json()
        if object_response:
            self.date = object_response['response'][0]['risetime']
            self.duration = object_response['response'][0]['duration']
            self.remaining = object_response['response'][0][ 'risetime' ] - calendar.timegm(time.gmtime())
            self.time = AltTime().retrieve_time()         
