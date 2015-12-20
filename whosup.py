import nmap
from internet import internet

class whosup:

    def __init__(self):
        self.users_at_home()
    
    
    def sweep(self):
        nm = nmap.PortScanner()
        nm.scan(hosts = '192.168.0.0/24', arguments = '-n -sP -PE -T5')
        up_macs=[]
        print "=========================================================================="
        print "Starting new loop"
        ######### UPDATING DATABASE ##############
        for host in nm.all_hosts():	
        ######### LIST MAC ADDRESS ################
        # If the status of an element is not down, we print it
            if nm[host]['status']['state'] != "down":	
                try:
                    if str(nm[host]['addresses']['mac']) not in up_macs:
                    #print str(nm[host]['addresses']['mac'])
                        up_macs.append( str(nm[host]['addresses']['mac']))
					
                except:
                    mac = 'unknown'
        self.macs = up_macs

    def users_at_home(self):
        self.sweep()
        