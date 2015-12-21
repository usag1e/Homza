import nmap

class NetworkSweeper:
    def __init__(self):
        self.sweep()
    
    def sweep(self):
        nm = nmap.PortScanner()
        nm.scan(hosts = '192.168.0.0/24', arguments = '-n -sP -PE -T5')
        up_macs=[]
        ######### UPDATING DATABASE ##############
        for host in nm.all_hosts():	
        ######### LIST MAC ADDRESS ################
        # If the status of an element is not down, we print it
            print host
            if nm[host]['status']['state'] != "down":	
                try:
                    if str(nm[host]['addresses']['mac']) not in up_macs:
                        up_macs.append( str(nm[host]['addresses']['mac']))
                except:
                    mac = 'unknown'
        self.macs = up_macs
