# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 16:22:31 2015

@author: ilyass
"""
import time as pytime
import datetime
import math

class AltTime:
    def __init__(self):
        self.retrieve_time()     

    @classmethod
    def retrieve_time(klass):
        localtime = pytime.localtime()
        timeString = pytime.strftime("%Y%m%d%H%M%S", localtime)
        return timeString
