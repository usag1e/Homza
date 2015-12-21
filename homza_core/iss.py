# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 16:36:07 2015

@author: ilyass
"""
from house import House
from internet import Internet
import logging

logger = logging.getLogger(__name__)

class IssFinder:
    def __init__(self):
        self.next_passage()
        
    def next_passage(self):
        house = House()
        print house.latitude, house.longitude
        if not house.latitude and not house.longitude:
            print "IN IF"
            logger.error("Could not find latitude or longitude.")
            return False
        # Requesting ISS from Open-notify.org for Montreal, in .json
        print "Requesting"
        request_url = 'http://api.open-notify.org/iss-pass.json?lat=%s&lon=%s' % ( house.longitude, house.latitude )        
        response = Internet.get(request_url)
        print response
        object_response = response.json()
        if object_response:
            self.date = object_response['response'][0]['risetime']
            self.duration = object_response['response'][0]['duration']
            self.remaining = object_response['response'][0][ 'risetime' ] - calendar.timegm(time.gmtime())
