from Weather import getWeatherMontreal
from ISS import getISSMontreal
from Internet import CheckInternet
import Internet
import time

# This file will be regularly called by cron

getWeatherMontreal()
getISSMontreal()
CheckInternet(5)
