from Weather import getWeather
from ISS import getISS

# This file will be regularly called by cron

getWeather()
getISS()
