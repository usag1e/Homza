import time
from couchdb_handler import *

def retrieve_time():
	localtime=time.localtime()
	timeString =time.strftime("%Y%m%d%H%M%S",localtime)
	human_time=time.strftime("%Y/%m/%d  %H:%M:%S",localtime)
	return human_time

human_time=retrieve_time()

print human_time
print retrieve_time()



