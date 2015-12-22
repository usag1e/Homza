# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 16:22:31 2015

@author: ilyass
"""
import time
# print repr(time) # To debug an import !

class AltTime:
    def __init__(self):
        self.retrieve_time()     

    @classmethod
    def retrieve_time(klass):
        the_time = time.localtime()
        return time.strftime("%Y%m%d%H%M%S", the_time)
