import urllib2 
import logging

logger = logging.getLogger(__name__)

class Internet:

    def __init__(self):
        self.checkConnection()
    
    
    def checkConnection(self):
        try:
            urllib2.urlopen("http://www.google.com").close()
        except urllib2.URLError:
	    logger.warning("[internet] OFF")
            self.internet = False
        else:
	    logger.info("[internet] ON")
            self.internet = True
