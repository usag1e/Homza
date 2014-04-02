#I: D'ou tu peux ecrire import "nom_d'un_fichier_en_python"?
import Transportation
import Weather

# Some kind of main that will call the different functions to fetch data
# This file will be regularly called by cron

#I: C'est quoi cron?

##Test Pin is 5
GPIO.setup(5, GPIO.OUT)
##Test Pin is 7
GPIO.setup(7, GPIO.OUT)

def CheckInternet():
  while True:
      try:
	  urllib2.urlopen("http://www.google.com").close()
      except urllib2.URLError:
	  print "Not Connected"
	  GPIO.output(5, True)
	  time.sleep(10)
      else:
	  print "Connected"
	  GPIO.output(7, False)
	  break

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
        
##Test Pin is 6
GPIO.setup(6, GPIO.OUT)

# Function to get the weather in Montreal
def getISSMontreal() :
    #Requesting ISS from Open-notify.org for Montreal, in .json
    r = requests.get('http://api.open-notify.org/iss-pass.json?lat=45.5&lon=73.567')
    #extracting the .json data from the request
    rj = r.json()
    #Printing the whole .json thing, with pprint() 'cause they say it's nicer
    pprint(rj)
    #The API gives the date and time back as UNIX time, it must be converted, here we select the date from the json answer
    Date = rj['response'][0]['risetime']
    #Here we convert the UNIX answer to normal date and time
    print('The ISS will be visible at', datetime.datetime.fromtimestamp(Date).strftime("%R:%S, %B %d, %Y"))
    Date = datetime.datetime.fromtimestamp(Date)
    #The duration is given in seconds by the API, here we select the duration from the json answer
    Duration = rj['response'][0]['duration']
    print('The ISS will be visible for', Duration, 'seconds')
    
    #This section uses time stamps to determine if the ISS is currently in the air
    now = datetime.datetime.now()
    if Date.month == now.month:
      print('month OK')
      if Date.day == now.day:
	print('day OK')
	#print('Now=', now)
	#print('Date=', Date)
	nowsum = (now.hour*3600 + now.minute*60 + now.second)
	Datesum = (Date.hour*3600 + Date.minute*60 + Date.second)
	#print(nowsum)
	#print(Datesum)
	Diff = nowsum - Datesum
	if Diff > 0:
	  print('THE ISS IS VISIBLE NOW')
	  GPIO.output(6,True)
	else:
	  print('ISS currently not visible')
	  GPIO.output(6, True)

while True:
    getWeatherMontreal()
    time.sleep(600)

while True:
    getISSMontreal()
    time.sleep(30)
    
while True:
  CheckInternet()
  time.sleep(12)
getWeatherMontreal()
getTransportationInfoMontreal()