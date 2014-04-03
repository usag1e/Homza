#This one is necessary to print in a pretty way the .json answer. It's only for testing purpose.
from pprint import pprint
import requests
#This one is necessary to convert the time sent by the API in UNIX to normal date and time
import os, datetime
import RPi.GPIO as GPIO
import time

##Type numerotation choisie pour les PIN
GPIO.setmode(GPIO.BOARD)
##Test Pin is 3
GPIO.setup(3, GPIO.OUT)

# Function to get the weather in Montreal
def getISSMontreal() :
    #Requesting ISS from Open-notify.org for Montreal, in .json
    l = requests.get('http://api.open-notify.org/iss-pass.json?lat=45.5&lon=73.567')
    #extracting the .json data from the request
    lj = l.json
    #Printing the whole .json thing, with pprint() 'cause they say it's nicer
    #pprint(lj)
    #The API gives the date and time back as UNIX time, it must be converted, here we select the date from the json answer
    Date = lj['response'][0]['risetime']
    #Here we convert the UNIX answer to normal date and time
    print('The ISS will be visible at', datetime.datetime.fromtimestamp(Date).strftime("%R:%S, %B %d, %Y"))
    Date = datetime.datetime.fromtimestamp(Date)
    #The duration is given in seconds by the API, here we select the duration from the json answer
    Duration = lj['response'][0]['duration']
    print('The ISS will be visible for', Duration, 'seconds')
    
    #This section uses time stamps to determine if the ISS is currently in the air
    now = datetime.datetime.now()
    if Date.month == now.month:
      print('Now=', now.day)
      print('Date=', Date.da)
      if Date.day == now.day:
	nowsum = (now.hour*3600 + now.minute*60 + now.second)
	Datesum = (Date.hour*3600 + Date.minute*60 + Date.second)
	print(nowsum)
	print(Datesum)
	Diff = nowsum - Datesum
	print(Diff)
	if Diff > 0:
	  print('THE ISS IS VISIBLE NOW')
	  print('3 is ON')
	  GPIO.output(3,True)
	else:
	  print('ISS currently not visible')
	  print('3 is OFF')
	  GPIO.output(3, False)

