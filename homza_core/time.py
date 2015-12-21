# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 16:22:31 2015

@author: ilyass
"""
import time
import datetime
import math

class Time:
    def __init__(self):
        self.retrieve_time()        
        
        
    def retrieve_time(self):
        localtime=time.localtime()
        timeString =time.strftime("%Y%m%d%H%M%S", localtime)
        return timeString
