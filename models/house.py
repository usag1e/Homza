# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 17:26:41 2015

@author: ilyass
"""
import yaml, os
from . import Entity

class House:
    _collection = 'homza'

    def __init__(self, data):
        if not data:
            raise Entity.ArgumentMissingException('House.data')
        self._id = data['name']
        already_saved = super(House, self).get()
        if already_saved:
            self = already_saved
        else:
            self.longitude = data['longitude']
            self.latitude = data['latitude']
            self.create()
    
    @classmethod
    def init(klass):
        script_dir = os.path.dirname(__file__)
        with open(os.path.join(script_dir, "../data/house.yml"), 'r') as ymlfile:
            houseData = yaml.load(ymlfile)
            house = House(houseData)
            return house
