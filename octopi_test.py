import requests
from pprint import pprint
import json


r = requests.get('http://192.168.1.156/api/connection', auth=('API', '3D2318DE50E14E42AC2C804EC5DA4B81') )
print r.url
content = r.content
data = json.loads(content)
print "Printer Status:"
status = data['current']['state']
print data['current']['state']


r = requests.get('http://192.168.1.156/api/printer', auth=('API', '3D2318DE50E14E42AC2C804EC5DA4B81') )
print r.url
content = r.content
data = json.loads(content)
bed_temperature = data['temps']['bed']['actual']
print "Bed temperature:"
print bed_temperature
head_temperature = data['temps']['tool0']['actual']
print "Head temperature:"
print head_temperature

payload = {'state': 'true'}
r = requests.get('http://192.168.1.156/api/job', auth=('API', '3D2318DE50E14E42AC2C804EC5DA4B81') )
print r.url
content = r.content
data = json.loads(content)
job_name = data['job']['file']['name']
print "Job name:"
print job_name
completion = data['progress']['completion']
print "Completion:"
print completion
elapsed_print_time = data['progress']['printTime']
print "Elapsed print time:"
print elapsed_print_time
remaining_print_time = data['progress']['printTimeLeft']
print "Remaining print time:"
print remaining_print_time

