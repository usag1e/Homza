#You absolutely need these 2 imports at the beginning of your script to be able to use these functions, also you mest be in the same folder
from couchdb_handler import *
import time
import nmap

#Initialisation
user_mac=[]
unknown_mac=[]
up_macs=[]
up_users=0

#Checking MAC Address Status
#We create a nm object that will be used to scan the network
nm = nmap.PortScanner()
#We give the scan parameter, and perform the scan
nm.scan(hosts = '192.168.1.0/24', arguments = '-n -sP -PE -T5')


######### UPDATING DATABASE ##############
#while (internet_on()==True):
for host in nm.all_hosts():
#Initialize TIME
	human_time,timeString=retrieve_time()
	
######### LIST MAC ADDRESS ################

	# If the status of an element is not down, we print it
	if nm[host]['status']['state'] != "down":
		print
		try:
			print "MAC ADDRESS:", nm[host]['addresses']['mac']
			up_macs.append( str(nm[host]['addresses']['mac']))
		except:
			mac = 'unknown'
###########################################

print up_macs
known_macs=retrieve_known_macs()
print retrieve_known_macs()

######### AVAILABLE USERS ################
up_known_macs=compare_list(up_macs,known_macs)
nb_users_up= len(up_known_macs)
nb_users_unknown=len(up_macs)-len(up_known_macs)

print nb_users_up, "known users in range"
print nb_users_unknown, "unknown users in range"


print "Update done for: " 
for macs in up_known_macs:
	update_last_seen_time(retrieve_user_for_mac(macs),timeString)
	up_known_macs_name=retrieve_user_for_mac(macs)
	print up_known_macs_name
	

		
#for host in nm.all_hosts():
#	if nm[host]['status']['state'] != "down":
#		try:
#			check_users(nm[host]['addresses']['mac'],user_mac,unknown_mac)
#		except:
#			mac = 'unknown'
#print
#print "================"
#print "We have ",len(user_mac) ,"activated known users in range"
#for macs in user_mac:
#	retrieve_user_for_mac(macs)
#	update_last_seen_time( retrieve_user_for_mac(macs) , #human_time)
#print "================"
#print "We have ",len(unknown_mac)," unknown users in range"
#print "================"
#print user_mac
#print unknown_mac
#print "================"
		
###########################################


#Update a user's last_seen_time


	
