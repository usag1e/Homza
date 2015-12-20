# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 16:14:44 2015

@author: ilyass
"""
from couchdb import *

class database:
    def __init__():
        
    def connect_to_db():
        return Server('http://localhost:5984')
        
    def create_or_load_db( couch, database_name ):
        try:
            return couch[ database_name ]
        except:
            return couch.create( database_name )
        
    def retrieve_music(self, user):
        couch = self.connect_to_db()
        db = 
