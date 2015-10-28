#!/usr/bin/python
# -*- coding: utf-8 -*-
#import appindicator
import gobject
import urllib2
import xmltodict
import json
import io
import subprocess
from couchdb_handler import *

def getETMData():
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

		#print
		#print ETMdata
		#print 
		#print ETMdata['Root']['Ligne']

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
		update_metro_service( ordered_status )

	
	except:
		pass


getETMData()

