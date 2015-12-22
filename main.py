#!/usr/bin/python
from homza_core import *

    
sweeper = NetworkSweeper()
up_macs = sweeper.macs
present_inhabitants = User.get_all_with_mac_addresses(up_macs)
print present_inhabitants
