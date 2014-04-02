from pprint import pprint
import requests
import RPi.GPIO as GPIO
import time

##Type numerotation choisie pour les PIN
GPIO.setmode(GPIO.BOARD)
##Test Pin is 7
GPIO.setup(7, GPIO.OUT)

# Function to get the weather in Montreal
def getWeatherMontreal() :
    #Requesting weather from OpenWeatherMap for Montreal, in .json
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Montreal&mode=json&units=metric')
    #extracting the .json data from the request
    rj = r.json
    #Printing the whole .json thing, with pprint() 'cause they say it's nicer
    #pprint(rj)
    #Temperature is called 'temp' and indented in 'main', we retrieve it
    temperature = rj['main']['temp']
    print('The temperature in Montreal is:', temperature)
    description = rj['weather'][0]['description']
    print('The weather is', description)
    print('Interrupt with Ctrl+C')
    if temperature > 0:
        GPIO.output(7, True)
    else:
        GPIO.output(7, False)

# LED class definition : trying to create an object with two attribute
# color : HEXA ? word ? (Define the type of the attribute here)
# status : boolean

#I: Python etant dynamique, je devrais pouvoir attendre jusque la derniere minute pour faire de status une variable booleenne, mais je ne sais pas comment le faire...
class LED:
    def __init__(self, color, status):
        self.color = color
        self.status = status

LED_weather = LED("blue", "ON")

print("The LED is", LED_weather.color)
print("The LED is", LED_weather.status)

while True:
    getWeatherMontreal()
    time.sleep(600)
