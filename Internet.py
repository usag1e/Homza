import time
import urllib2 
import RPi.GPIO as GPIO
from DBhandler import insertInternet

GPIO.setmode(GPIO.BOARD)

def checkConnection():
    try:
        urllib2.urlopen("http://www.google.com").close()
    except urllib2.URLError:
	insertInternet( False )
        return False
    else:
	insertInternet( True )
        return True

def displayInternet(X):
    isConnected = checkConnection()
    if( isConnected == False ):
	print "[Internet] Not connected - %d is OFF" % X
	GPIO.output(X, False)
	time.sleep(2)
    else:
	print "[Internet] Connected - %d is ON" % X
	GPIO.output(X, True)
	time.sleep(2)
