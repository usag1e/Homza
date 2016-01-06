#!/usr/bin/python
from homza_core import *
from multiprocessing import Process
import time

#up_macs = sweeper.macs
#present_inhabitants = User.get_all_with_mac_addresses(up_macs)
#for user in present_inhabitants:
#    print user._id + ' detected'
    
iss = IssFinder()
weather = WeatherCenter()
subway = Subway()

i = 0

while True:
    processes = []
    sweeper = NetworkSweeper()
    p1 = Process( target = sweeper )
    processes.append(p1)
    i = i + 1
    
    if i > 10:
        p2 = Process( target = iss )
        p3 = Process( target = weather )
        p4 = Process( target = subway )
        processes.append( p2 )
        processes.append( p3 )
        processes.append( p4 )
        i = 0
        
    for pr in processes:
        pr.start()
    for pr in processes:
        pr.join()
    sweeper.sweep()
    up_macs = sweeper.macs
    present_inhabitants = User.get_all_with_mac_addresses(up_macs)
    time.sleep(0.3)
    
    
