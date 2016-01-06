import nmap
from entity import Entity
import logging
#from user import User
import pydash as _
from alttime import AltTime

logger = logging.getLogger(__name__)

class NetworkSweeper(Entity):
    _collection = 'homza'
    _type = 'network'
    
    def __init__(self):
        logger.info("Initialized sweeper object")
    
    def __call__(self):
        self.sweep()
    
    def sweep(self):
        up_macs=[]
        for i in range(0,3):
            nm = nmap.PortScanner()
            nm.scan(hosts = '192.168.1.0/24', arguments = '-n -sP -PE -T5')
            up_macs=[]
            ######### UPDATING DATABASE ##############
            for host in nm.all_hosts():	
            ######### LIST MAC ADDRESS ################
            # If the status of an element is not down, we print it
                if nm[host]['status']['state'] != "down":	
                    try:
                        if str(nm[host]['addresses']['mac']) not in up_macs:
                            up_macs.append( str(nm[host]['addresses']['mac']))
                    except:
                        mac = 'unknown'
        print up_macs
        self.macs = up_macs

    #This function writes in couchdb each time a MAC address connects to the 
    #network after an hour, and the time at which a MAC address disappears
    #from the network
    #By correlating this information and your own information on who is present
    #your physical space or not, you can guess who owns each MAC address
    def identify_unknowns(self, one_mac):
        print "In identify", one_mac
        self.type = NetworkSweeper._type
        self._id = one_mac
        already_saved = self.get()
        detected_time = AltTime.retrieve_time()
        if already_saved is not None:
            self = already_saved
            #If the unkown mac address disappeared more than an hour ago, then 
            #its owner pbly left an hour ago
            if (int(detected_time)-int(self.time[len(self.time)-1])) > 3600:
                self.time_out.append(self.time[len(self.time)-1])
                #Since we just detected this mac when it wasnt here for more 
                #than an hour it means that its owner pbly just came in
                self.time_in.append(detected_time)
            self.time.append(detected_time)
            self.create()
        #If first time we see this unkown MAC address, we need to init the 
        #couchdb object
        else:
            self.time = []
            self.time.append(detected_time)
            self.time_out = []
            self.time_in = []
            self.create()
