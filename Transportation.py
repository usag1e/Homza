# Warning: This program can take some time to fecth the times from the STM of Montreal.

# Import the librairy needed to fetch data from a url
import urllib2

def getTransportationInfoMontreal() :
    # The transportation data is provided in GTFS (General Transit Feed Specification)
    time_Montreal = urllib2.urlopen( "http://www.stm.info/sites/default/files/gtfs/gtfs_stm.zip" )
    #the 'wb' in open('test.mp3','wb') opens a (and erases any existing) file, binaraly, so you can save data with it, instead of just text.
    output = open('Montreal.zip','wb')
    output.write('transporation/',time_Montreal.read())
    output.close()

# Ce bout fonctionne, et telecharge dans le dossier ou se trouve Transportation.py le fichier Montreal.zip qui contient les horaires et tout
