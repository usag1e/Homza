import os
import time
import urllib2 
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

def checkConnection():
    try:
        urllib2.urlopen("http://www.google.com").close()
    except urllib2.URLError:
        return False
    else:
        return True

def CheckInternet(X):
	GPIO.setup(7, GPIO.OUT)
	isConnected = checkConnection()
	if( isConnected == False ):
		print "Not Connected"
		print X, "is OFF"
		GPIO.output(X, False)
		time.sleep(2)
	else:
		print "Connected"
		print X, "is ON"
		GPIO.output(X, True)
		time.sleep(2)
	GPIO.cleanup()

CheckInternet(7)



