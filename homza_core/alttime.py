# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 16:22:31 2015

@author: ilyass
"""
import time
from datetime import datetime
# print repr(time) # To debug an import !

class AltTime:
    def __init__(self):
        self.retrieve_time()     

    @classmethod
    def retrieve_time(klass):
        the_time = time.localtime()
        return time.strftime("%Y%m%d%H%M%S", the_time)
    
    @classmethod
    def human_time(klass, couchdb_time):
        the_time = datetime.strptime(couchdb_time, "%Y%m%d%H%M%S")
        return the_time
