#This one is necessary to print in a pretty way the .json answer. It's only for testing purpose.
from pprint import pprint
from DBhandler import getHomeFromDB, insertIss, getIssDateFromDB, getIssDurationFromDB
import requests
#This one is necessary to convert the time sent by the API in UNIX to normal date and time
import datetime
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
    iss_date = getIssDateFromDB()
    print iss_date
    #This section uses time stamps to determine if the ISS is currently in the air
    now = datetime.datetime.now()
    if Date.month == now.month:
      if Date.day == now.day:
	iss_duration = getIssDurationFromDB()
	nowsum = (now.hour*3600 + now.minute*60 + now.second)
	Datesum = (Date.hour*3600 + Date.minute*60 + Date.second)
	#print(nowsum)
	#print(Datesum)
	Diff = nowsum - Datesum
	#print(Diff)
	if Diff > 0:
	  print( '[ISS] The ISS is visible now - %d is ON' % X )
	  GPIO.output( X, True )
	else:
	  print( '[ISS] The ISS is not visible now - %d is OFF' % X )
	  GPIO.output( X, False )
      else:
	print( '[ISS] Today is not a good day - %d is OFF' % X )
	GPIO.output( X, False )  

