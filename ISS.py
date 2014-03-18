from pprint import pprint
import requests

# Function to get the weather in Montreal
def getISSMontreal() :
    #Requesting ISS from Open-notify.org for Montreal, in .json
    r = requests.get('http://api.open-notify.org/iss-pass.json?lat=45.5&lon=73.567')
    #extracting the .json data from the request
    rj = r.json()
    #Printing the whole .json thing, with pprint() 'cause they say it's nicer
    pprint(rj)
    
getISSMontreal()