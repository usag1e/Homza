# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 17:26:41 2015

@author: ilyass
"""

class house:
    
    def __init__(self):
        self.import_house()
        
    def import_house(self):
        script_dir = os.path.dirname(__file__)
        try:
            with open(os.path.join(script_dir, "users.yml"), 'r') as ymlfile:
                house = yaml.load(ymlfile)
                self.ymlfile = house
                return users
        except Exception as e:
            raise e