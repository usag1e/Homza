#!/usr/bin/python
from homza_core import *


sweeper = NetworkSweeper()
up_macs = sweeper.macs
present_inhabitants = User.get_all_with_mac_addresses(up_macs)
for user in present_inhabitants:
    print user._id + ' detected'
    
iss = IssFinder()
weather = WeatherCenter()

