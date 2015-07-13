#!/usr/bin/python
# -*- coding: utf-8 -*-
#import appindicator
import gobject
import urllib2
import xmltodict
import json
import io
import subprocess

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

		#print
		#print ETMdata
		#print 
		#print ETMdata['Root']['Ligne']

		for ligne in ETMdata['Root']['Ligne']:
			#These commands show the information we need from the dictionary
			print ligne['NoLigne'], ligne['msgAnglais'].encode('utf-8') 
			print ""

			if ligne['msgAnglais'].encode('utf-8') == "Normal métro service.": 
 				metrostatus[int(ligne['NoLigne'])] = False
				metromsg[int(ligne['NoLigne'])] = ligne['msgAnglais'].encode('utf-8')
			else:
				print "Not in Normal Metro situation"
				metrostatus[int(ligne['NoLigne'])] = True
				metromsg[int(ligne['NoLigne'])] = ligne['msgAnglais'].encode('utf-8')


		#if (len(set(metrostatus.items()) & set(self.metrostatus.items())) != 4):
		#	if (len(set(self.metrostatusclear.items()) & set(metrostatus.items())) == 4):
		#		subprocess.Popen(["aplay", "timbre3_speciaux_perturbations.wav"])
		#	else:
		#		subprocess.Popen(["aplay", "timbre1_clientele.wav"])

	
	except:
		pass


getETMData()

