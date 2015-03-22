import os
import shlex
import subprocess
#import datetime
#import random
#import glob
#import json
import sys
import time
#from easyprocess import Proc
from threading import Timer
from couchdb_handler import *

def program_exists(name):
	try:
		subprocess.check_output("which {0}".format(name), shell=True)
		return True
	except:
		#print "ERROR: {0} Not found".format(name)
		return False

def audio_player_name():
	for name in ['mplayer', 'omxplayer', 'afplay']:
		if program_exists(name):
			return name

	sys.exit('No audio player found. We recommend installing mplayer')


def play_song(user):			
	file_to_play = retrieve_music(user)
	if not file_to_play:
		return False #greet(user)

	audio_player = audio_player_name()
	cmd_string = "{0} \"{1}\"".format(audio_player, file_to_play)
	print cmd_string
	cmd=shlex.split(cmd_string)		

	proc = Process_runner(cmd_string, 20)	
	#stdout=Proc(cmd).call(timeout=10).stdout

	#player = subprocess.Popen([audio_player, "-o", "local", file_to_play], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	#time.sleep(self.config['song_timeout'])		
	#player.stdin.write("\x03");
	#player.stdin.write("q")
		
	#stdout=Proc(cmd).call(timeout=10).stdout
	#stdout=Proc(["/usr/bin/omxplayer", "-o", "local", file_to_play]).call(timeout=10).stdout

	
class Process_runner:
	def __init__(self, cmd, timeout):
		self.run(cmd, timeout)

	@staticmethod
	def kill_proc(proc, timeout):
		timeout["value"] = True
		proc.kill()

	def run(self, cmd, timeout_sec):
		proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		timeout = {"value": False}
		timer = Timer(timeout_sec, self.kill_proc, [proc, timeout])
		timer.start()
		stdout, stderr = proc.communicate()
		timer.cancel()
		return proc.returncode, stdout.decode("utf-8"), stderr.decode("utf-8"), timeout["value"]
 
	
def unique_user_for_macs(list_macs):
	users=[]
	for mac in list_macs:
		user=retrieve_user_for_mac(mac)
		if user not in users:
			users.append(user)
	return users


