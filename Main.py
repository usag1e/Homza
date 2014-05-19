from Weather import getWeatherMontreal
from ISS import getISSMontreal
from Internet import CheckInternet
import Internet
import time
import RPi.GPIO as GPIO

# Some kind of main that will call the different functions to fetch data
# This file will be regularly called by cron

while True:
    getWeatherMontreal()
    getISSMontreal()
    CheckInternet(5)
    time.sleep(20)
