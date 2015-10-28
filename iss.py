#This one is necessary to print in a pretty way the .json answer. It's only for testing purpose.
from pprint import pprint
import requests
#This one is necessary to convert the time sent by the API in UNIX to normal date and time
import datetime
import time
import calendar
from couchdb_handler import *

# Function to get the weather in Montreal
def getISS() :
	#home = getHomeFromDB()
	# Requesting ISS from Open-notify.org for Montreal, in .json
	request_url = 'http://api.open-notify.org/iss-pass.json?lat=%s&lon=%s' % ( 45.50, -73.56 )
	# print request_url
	l = requests.get( request_url )
	# extracting the .json data from the request
	lj = l.json()
	# Printing the whole .json thing, with pprint() 'cause they say it's nicer
	# pprint(lj)
	# The API gives the date and time back as UNIX time, it must be converted, here we select the date from the json answer
	date = lj['response'][0]['risetime']
	duration = lj['response'][0]['duration']
	remaining = lj['response'][0][ 'risetime' ] - calendar.timegm(time.gmtime())
	# Here we convert the UNIX answer to normal date and time
	print '[iss] In ', remaining , "seconds; at", datetime.datetime.fromtimestamp(date).strftime("%R:%S, %B %d, %Y"), "for", duration, 'seconds'
	update_ISS_passage( remaining, duration, datetime.datetime.fromtimestamp(date).strftime("%R:%S, %B %d, %Y") )

getISS()


