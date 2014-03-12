#CE PROGRAMME MET DU TEMPS A S'EXECUTER CAR IL SE CONNECTE EN LIGNE ET TELECHARGE LES HORAIRES DE LA STM DE MONTREAL. CA PEUT PRENDRE DU TEMPS.

#Librairie necessaire pour telecharger des fichiers... il parait
import urllib2

#La ville de Montreal fournit les donnes transports sous format GTFS
time_Montreal = urllib2.urlopen("http://www.stm.info/sites/default/files/gtfs/gtfs_stm.zip")
#the 'wb' in open('test.mp3','wb') opens a (and erases any existing) file, binaraly, so you can save data with it, instead of just text.
output = open('Montreal.zip','wb')
output.write(time_Montreal.read())
output.close()

#Ce bout fonctionne, et telecharge dans le dossier ou se trouve Transportation.py le fichier Montreal.zip qui contient les horaires et tout
