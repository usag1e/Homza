#I: D'ou tu peux ecrire import "nom_d'un_fichier_en_python"?
from Weather import getWeatherMontreal
from ISS import getISSMontreal
from Internet import CheckInternet
import Internet
import time

# Some kind of main that will call the different functions to fetch data
# This file will be regularly called by cron

#I: C'est quoi cron?

##Type numerotation choisie pour les PIN
GPIO.setmode(GPIO.BOARD)
##Test Pin is 7
GPIO.setup(7, GPIO.OUT)
##Test Pin is 3
GPIO.setup(3, GPIO.OUT)
##Test Pin is 5
GPIO.setup(5, GPIO.OUT)


while True:
    getWeatherMontreal()
    getISSMontreal()
    CheckInternet(5)
    time.sleep(20)
