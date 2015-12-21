import urllib2 
import logging
import requests

logger = logging.getLogger(__name__)

class Internet:
    def __init__(self):
        self.checkConnection()
    
    @classmethod
    def get(klass, url):
        try:
            return requests.get(url)
        except:
            return False
    
    def checkConnection(self):
        try:
            urllib2.urlopen("http://www.google.com").close()
        except urllib2.URLError:
	    logger.warning("[internet] OFF")
            self.internet = False
        else:
	    logger.info("[internet] ON")
            self.internet = True
