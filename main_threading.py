#!/usr/bin/python
from homza_core import *
from multiprocessing import Process
import time


sweeper = NetworkSweeper()
#up_macs = sweeper.macs
#present_inhabitants = User.get_all_with_mac_addresses(up_macs)
#for user in present_inhabitants:
#    print user._id + ' detected'
    
iss = IssFinder()
weather = WeatherCenter()


i = 0

while True:
    processes = []
    p1 = Process( target = sweeper )
    processes.append(p1)
    i = i + 1
    
    if i > 3:
        p2 = Process( target = iss )
        p3 = Process( target = weather )
        processes.append( p2 )
        processes.append( p3 )
        i = 0
        
    for pr in processes:
        pr.start()
    for pr in processes:
        pr.join()
    up_macs = sweeper.macs
    present_inhabitants = User.get_all_with_mac_addresses(up_macs)
    time.sleep(2)
    
    
