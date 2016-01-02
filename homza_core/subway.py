# -*- coding: utf-8 -*-
from internet import Internet
import logging
import requests
import datetime
import time
from entity import Entity
import gobject
import urllib2
import xmltodict
import json
import io
import subprocess

logger = logging.getLogger(__name__)

class Subway(Entity):
    _collection = 'homza'
    _type = 'subway'

    def __init__(self):
        self._id = "subway"
        self.type = Subway._type
        self.getSubway()
        self.update()
        logger.info("Updated Subway data.")
        
    def __call__(self):
        self.__init__()
           
    def getSubway(self):
	try:
            ETMfile = urllib2.urlopen('http://www2.stm.info/1997/alertesmetro/esm.xml')
            #An XML file is retrieved from the API
            ETMdata = ETMfile.read()
            ETMfile.close()
            #The XML data is transformed into a set of dictionaries
            ETMdata = xmltodict.parse(ETMdata)
    
            metrostatus = {}
            metromsg = {}
            ordered_status = []


            for ligne in ETMdata['Root']['Ligne']:
                #These commands show the information we need from the dictionary
                if ligne['msgAnglais'].encode('utf-8') == "Normal métro service.": 
                    metrostatus[int(ligne['NoLigne'])] = False
                    ordered_status.append(False)
                    print "[status_metro] ", ligne['NoLigne'], ligne['msgAnglais'].encode('utf-8') 
                    metromsg[int(ligne['NoLigne'])] = ligne['msgAnglais'].encode('utf-8')
                else:
                    metrostatus[int(ligne['NoLigne'])] = True
                    ordered_status.append(True)
                    print "[status_metro] ", ligne['NoLigne'], ligne['msgAnglais'].encode('utf-8') 
                    metromsg[int(ligne['NoLigne'])] = ligne['msgAnglais'].encode('utf-8')
                #print len(metrostatus), metrostatus
                #update_metro_service( ordered_status )#old function from before refactory

            time_of_treatment = (datetime.datetime.fromtimestamp(int(time.mktime(time.localtime()))).strftime('%Y%m%d%H%M%S'))
            print ordered_status
            #for ligne in ordered_status
            self.time = time_of_treatment
            self.metro1=ordered_status[0]
            self.metro2=ordered_status[1]
            self.metro4=ordered_status[2]
            self.metro5=ordered_status[3]
	except:
            pass

