import RPi.GPIO as GPIO
from Weather import displayWeather
from ISS import displayISS
from Internet import displayInternet
import time
import signal
import sys

def signal_handler(signal, frame):
    print('You pressed Ctrl+C! Bye :)')
    # Clean
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

GPIO.setmode( GPIO.BOARD )

interval_check_weather = 120 # in seconds
interval_check_internet = 5 # in seconds
XISS = 3
XWeather = 5
XTransportation = 9
XInternet = 7 
# ISS
GPIO.setup( XISS, GPIO.OUT )
# Weather
GPIO.setup( XWeather, GPIO.OUT )
# Transportation
# GPIO.setup( XTransportation, GPIO.OUT )
# Internet
GPIO.setup( XInternet, GPIO.OUT )

# Check infos in the DB regularly
while 1:
    displayISS( XISS ) 
    displayWeather( XWeather )
    for i in range( 0, interval_check_weather/interval_check_internet ):
	displayInternet( XInternet )
	time.sleep( interval_check_internet )

