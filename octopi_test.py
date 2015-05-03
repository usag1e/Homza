import requests
from pprint import pprint
import json

def retrieve_printer_status():
	status = {}

	r = requests.get('http://192.168.1.156/api/connection', auth=('API', '3D2318DE50E14E42AC2C804EC5DA4B81') )
	content = r.content
	data = json.loads(content)
	printer_status = data['current']['state']
	status['printer_status'] = printer_status

	r = requests.get('http://192.168.1.156/api/printer', auth=('API', '3D2318DE50E14E42AC2C804EC5DA4B81') )
	content = r.content
	data = json.loads(content)
	bed_temperature = data['temperature']['temps']['bed']['actual']
	status['bed_temperature'] = bed_temperature
	head_temperature = data['temperature']['temps']['tool0']['actual']
	status['head_temperature'] = head_temperature

	payload = {'state': 'true'}
	r = requests.get('http://192.168.1.156/api/job', auth=('API', '3D2318DE50E14E42AC2C804EC5DA4B81') )
	content = r.content
	data = json.loads(content)
	job_name = data['job']['file']['name']
	status['job_name'] = job_name	
	completion = data['progress']['completion']
	status['completion'] = completion
	elapsed_print_time = data['progress']['printTime']
	status['elapsed_print_time'] = elapsed_print_time
	remaining_print_time = data['progress']['printTimeLeft']
	status['remaining_print_time'] = remaining_print_time
	return status


