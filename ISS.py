#This one is necessary to print in a pretty way the .json answer. It's only for testing purpose.
from pprint import pprint
from DBhandler import getHomeFromDB, insertIss, getIssDateFromDB, getIssDurationFromDB
import requests
#This one is necessary to convert the time sent by the API in UNIX to normal date and time
import datetime
import time
import calendar
import RPi.GPIO as GPIO

# Function to get the weather in Montreal
def getISS() :
    home = getHomeFromDB()
    # Requesting ISS from Open-notify.org for Montreal, in .json
    request_url = 'http://api.open-notify.org/iss-pass.json?lat=%s&lon=%s' % (home.lat, home.lon)
    # print request_url
    l = requests.get( request_url )
    # extracting the .json data from the request
    lj = l.json()
    # Printing the whole .json thing, with pprint() 'cause they say it's nicer
    # pprint(lj)
    for response in lj[ 'response' ]:
	# The API gives the date and time back as UNIX time, it must be converted, here we select the date from the json answer
	Date = response[ 'risetime' ]
	# Here we convert the UNIX answer to normal date and time
	# print('The ISS will be visible at', datetime.datetime.fromtimestamp(Date).strftime("%R:%S, %B %d, %Y"))
	# Date = datetime.datetime.fromtimestamp(Date)
	# The duration is given in seconds by the API, here we select the duration from the json answer
	Duration = response[ 'duration' ]
	# print('The ISS will be visible for', Duration, 'seconds')
	insertIss( Date, Duration )
    
def displayISS( X ) :
    # Get the date just older than right now (so, the most recent past date)
    iss_db_date = getIssDateFromDB()
    if iss_db_date != None:
	iss_date = [ 'date' ] 
        # print iss_date
        #This section uses time stamps to determine if the ISS is currently in the air
        now = datetime.datetime.now()
        if iss_date.month == now.month:
          if iss_date.day == now.day:
            timestamp_date = calendar.timegm( iss_date.timetuple() )
            print timestamp_date
            iss_duration = getIssDurationFromDB( timestamp_date )
            timestamp_now = calendar.timegm( iss_date.timetuple() )
            time_elapsed = ( timestamp_now - timestamp_date ) # (until positive : invisible) 
            time_left = ( timestamp_date + duration ) - timestamp_now # (as long as is positive : visible)
            if time_elapsed > 0 and time_left > 0:
              print '[ISS] The ISS is visible now - %d is ON' % X 
              print "[ISS] visible since %d s and %d s left" % ( time_elapsed, time_left ) 
              GPIO.output( X, True )
            else:
              print '[ISS] The ISS is not visible now - %d is OFF' % X 
              GPIO.output( X, False )
          else:
	    print '[ISS] Today is not a good day - %d is OFF' % X
    else:
	print '[ISS] No date could be retrieved'


