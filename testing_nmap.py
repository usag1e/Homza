#This software is necessary: sudo apt-get install nmap
#Also sudo pip install python-pip
import nmap
import time

#We create a nm object that will be used to scan the network
nm = nmap.PortScanner()
#We give the scan parameter, and perform the scan
nm.scan(hosts = '192.168.1.0/24', arguments = '-n -sP -PE -T5')

#Recording local time of the scan in the object localtime using a function from the time package
localtime = time.asctime(time.localtime(time.time()))
#Printing time on screen
print('============ {0} ============'.format(localtime))

#Since we performed the scan, the function of nm, all_hosts() can be used to get the result of the scan as a list
#We go through each element of the list
for host in nm.all_hosts():
	# If the status of an element is not down, we print it
	if nm[host]['status']['state'] != "down":
		print 
		print "(In IF loop)"
		print "IP ADDRESS:", host
		print "STATUS:", nm[host]['status']['state']
		try:
			print "MAC ADDRESS:", nm[host]['addresses']['mac']
		except:
			mac = 'unknown'
