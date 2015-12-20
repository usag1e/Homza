# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 15:45:37 2015

@author: ilyass
"""
import logging
from process_runner import ProcessRunner

logger = logging.getLogger(__name__)


class MusicPlayer:
    def __init__(self, file_to_play):
        self.file_to_play = file_to_play
        self.play_song()

    def program_exists(self, name):
        try:
            subprocess.check_output("which {0}".format(name), shell=True)
            return True
        except:
            logger.warning("No music player found. No music will be played.")
            return False
    
    def audio_player_name(self):
        #Removed omxplayer. Weird results.
        for name in ['mplayer', 'afplay']:
            if self.program_exists(name):
                return name
        sys.exit('No audio player found. We recommend installing mplayer')
        
    def play_song(self):
        if not self.file_to_play:
            return False
        audio_player = self.audio_player_name()
        cmd_string = "{0} \"{1}\"".format(audio_player, self.file_to_play)
        logger.info(cmd_string)
        cmd = shlex.split(cmd_string)
        proc = Process_runner(cmd_string, 20)
        
