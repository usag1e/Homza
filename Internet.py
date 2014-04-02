import os
import time
import urllib2 
import RPi.GPIO as GPIO

##Type numerotation choisie pour les PIN
GPIO.setmode(GPIO.BOARD)
##Test Pin is 5
GPIO.setup(5, GPIO.OUT)

def CheckInternet():
  while True:
      try:
	  urllib2.urlopen("http://www.google.com").close()
      except urllib2.URLError:
	  print "Not Connected"
	  GPIO.output(5, True)
	  time.sleep(10)
      else:
	  print "Connected"
	  GPIO.output(5, False)
	  break


