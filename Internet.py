import os
import time
import urllib2 
import RPi.GPIO as GPIO

def CheckInternet(X):
  while True:
      try:
	  urllib2.urlopen("http://www.google.com").close()
      except urllib2.URLError:
	  print "Not Connected"
	  print X, "is ON"
	  GPIO.output(X, True)
	  time.sleep(10)
      else:
	  print "Connected"
	  print X, "is OFF"
	  GPIO.output(X, False)
	  break
      GPIO.cleanup()


