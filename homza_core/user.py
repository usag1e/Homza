import pydash as _
import yaml, os
from entity import Entity
from music_player import MusicPlayer
from alttime import AltTime
import logging
import sys
sys.setrecursionlimit(10000)

logger = logging.getLogger(__name__)

class User(Entity):
    _collection = 'homza'
    _type = 'user'

    def __init__(self, name, mac_addresses=[], image=None, song=None):
        self.type = User._type
        if not name:
            raise Entity.ArgumentMissingException('User.name')
        self._id = name
        already_saved = self.get()
        if already_saved is not None:
            self = already_saved
            self.update_my_status()
        else:
            self.mac_addresses = mac_addresses
            if image:
                self.image = image
            if song:
                self.song = song
            self.create()
    
    def play_song(self):
        MusicPlayer(self.song).play_song()
        
    def update_my_time(self):
        extime = AltTime.retrieve_time()
        detected_time = extime
        #Check if the inhabitant just arrived 
        #See if was here last loop but not here the onw before
        try:
            if int(self.time[-1])- int(self.time[-2])>1500:
                print self.time[-1], self.time[-2], int(self.time[-1])-int(self.time[-2])
                self.play_song()
        except:
            pass
        #Record time and date of the detection
        try:    
            self.time.append(detected_time)
        except:
            self.time = []
            self.time.append(detected_time)
        self.create()

    def update_my_status(self):
        time_now = AltTime.retrieve_time()
        try:
            for moment in self.time:
                if int(time_now) - int(moment) < 780:
                    self.status = "here"                    
                else:
                    self.status = "not_here"
                #logger.info("%s status is updated as %s" % (self._id, self.status)) 
        except AttributeError:
            pass
        
        

    @classmethod
    def get_all_with_mac_addresses(klass, mac_addresses):
        all_users = klass.get_all()
        filtered_users = _.collections.filter_(
            all_users,
            lambda user: any(
                one_mac for one_mac in user.mac_addresses if one_mac in mac_addresses
            )
        )
        for user in filtered_users:
            user.update_my_time()
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

