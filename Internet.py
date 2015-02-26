import time
import urllib2 


def checkConnection():
    try:
        urllib2.urlopen("http://www.google.com").close()
    except urllib2.URLError:
	print "[internet] OFF"
        return False
    else:
	print "[internet] ON"
        return True
