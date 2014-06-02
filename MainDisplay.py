import RPi.GPIO as GPIO
from Weather import displayWeather
from ISS import displayISS
from Internet import displayInternet
import time

GPIO.setmode( GPIO.BOARD )

interval_check_weather = 300
interval_check_internet = 20
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

# Clean
GPIO.cleanup()
