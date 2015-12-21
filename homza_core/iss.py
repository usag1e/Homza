# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 16:36:07 2015

@author: ilyass
"""
from house import House
from internet import Internet

class IssFinder:
    def __init__(self):
        self.next_passage()
        
    def next_passage(self):
        house = House()
        if not house.latitude or house.longitude:
            logger.error("Could not find latitude or longitude.")
            return False
        # Requesting ISS from Open-notify.org for Montreal, in .json
        request_url = 'http://api.open-notify.org/iss-pass.json?lat=%s&lon=%s' % ( house.longitude, house.latitude )        
        response = Internet.get(request_url)
        object_response = response.json()
        if object_response:
            self.date = object_response['response'][0]['risetime']
            self.duration = object_response['response'][0]['duration']
            self.remaining = object_response['response'][0][ 'risetime' ] - calendar.timegm(time.gmtime())
