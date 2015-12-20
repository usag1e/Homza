# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 15:57:52 2015

@author: ilyass
"""
import os
import shlex
import subprocess
import sys, time
from threading import Timer

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
        
        