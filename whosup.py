import nmap
from class_internet import internet

class whosup():

    def __init__(self):
        self.sweep()
        
        while True:
	        while (internet.status == True):
		        a=0
		        while ( a < 3 ):
			        nm = nmap.PortScanner()
			        nm.scan(hosts = '192.168.0.0/24', arguments = '-n -sP -PE -T5')
			        up_macs=[]
			        print "=========================================================================="
			        print "Starting new loop"
			        timeString = retrieve_time()
			        print "Time:", timeString
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
			        ###########################################

			        #print "UP MACS: ", up_macs
			        known_macs=retrieve_known_macs()
			        #print "KNOWN MACS: ",retrieve_known_macs()

			        ######### AVAILABLE USERS ################
			        up_known_macs=compare_list(up_macs,known_macs)
			        nb_users_up= len(up_known_macs)
			        nb_users_unknown=len(up_macs)-len(up_known_macs)

			        print nb_users_up, "known devices in range"
			        print nb_users_unknown, "unknown devices in range"


			        print "HERE: " 
			        for macs in up_known_macs:
				        update_last_seen_time(retrieve_user_for_mac(macs),timeString)
				        up_known_macs_name=retrieve_user_for_mac(macs)
				        print "User:", retrieve_user_for_mac(macs)
				        inhabitant_just_arrived(retrieve_user_for_mac(macs) )
				        if  inhabitant_just_arrived(retrieve_user_for_mac(macs) ) == True:	
					        print "Enjoy your song ! Now playing ..."
					        play_song(retrieve_user_for_mac(macs))
    
    
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
    
    
