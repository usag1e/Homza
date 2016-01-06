import pydash as _
import yaml, os
from entity import Entity
from music_player import MusicPlayer
from alttime import AltTime
import logging
import sys
from network_sweeper import NetworkSweeper
sys.setrecursionlimit(10000)

logger = logging.getLogger(__name__)

class User(Entity):
    _collection = 'homza'
    _type = 'user'
    who_knows_delay = 10 # minutes
    away_delay = 30 # minutes

    def __init__(self, name, mac_addresses=[], image=None, song=None, update_time=False):
        self.type = User._type
        if not name:
            raise Entity.ArgumentMissingException('User.name')
        self._id = name
        already_saved = self.get()
        if already_saved is not None:
            self = already_saved
            self.update_my_time(update_time)
        else:
            self.mac_addresses = mac_addresses
            if image:
                self.image = image
            if song:
                self.song = song
            self.create()
    
    def play_song(self):
        MusicPlayer(self.song).play_song()
        
    def update_my_time(self, update_time):
        extime = AltTime.retrieve_time()
        detected_time = extime
        #Check if the inhabitant just arrived 
        #See if was here last loop but not here the onw before
        try:
            print "%s was here last %s seconds ago" % (self._id, int(detected_time) - int(self.time[-1]))
        except:
            pass
        if update_time:
            self.isHere = 1
            try:
                if int(detected_time) - int(self.time[-1]) > 60 * User.away_delay:
                    self.play_song()
                if len(self.time) >= 100:
                    self.time.pop(0)
                self.time.append(detected_time)
            except:
                self.play_song()
                self.time = []
                self.time.append(detected_time)
        else:
            try:
                if (int(detected_time) - int(self.time[-1])) > 60 * User.who_knows_delay or len(self.time) is 0:
                    self.isHere = 0
                if (int(detected_time) - int(self.time[-1])) > 60 * User.away_delay:
                    self.isHere = -1
            except:
                self.isHere = 0
        self.create()
        

    @classmethod
    def get_all_with_mac_addresses(klass, mac_addresses):
        all_users = klass.get_all()
        filtered_users = _.collections.filter_(
            all_users,
            lambda user: any(
                one_mac for one_mac in user.mac_addresses if one_mac in mac_addresses
            )
        )
        #Let's get all the known macs in one list to find the unkowns
        #print "MAC ADDRESSES:", mac_addresses
        all_known_macs = []
        for user in filtered_users:
            all_known_macs.append(user.mac_addresses)
        #print "all_known_macs", all_known_macs
        
        #Now let's create unkown objects and 
        for one_mac in mac_addresses:
           if one_mac not in all_known_macs:
                network = NetworkSweeper()
                network.identify_unknowns(one_mac)
        
        #Let's update the known users we found on the network
        for user in filtered_users:
            user.update_my_time(True)
            logger.info("%s is home" % user._id)
        return filtered_users

    @classmethod
    def init(klass):
        script_dir = os.path.dirname(__file__)
        try:
            with open(
                os.path.join(script_dir, "../data/users.yml"), 'r'
            ) as ymlfile:
                users = yaml.load(ymlfile)
                users_list = []
                for user in users:
                    users_list.append(
                        User(
                            user["name"],
                            user["mac_addresses"],
                            user["image"],
                            user["song"]
                        )
                    )
                return users_list
        except Exception as e:
            raise e

