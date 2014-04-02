#I: D'ou tu peux ecrire import "nom_d'un_fichier_en_python"?
import Weather
import ISS
import Internet

# Some kind of main that will call the different functions to fetch data
# This file will be regularly called by cron

#I: C'est quoi cron?



while True:
    getWeatherMontreal()
    CheckInternet()
    getISSMontreal()
    time.sleep(20)
