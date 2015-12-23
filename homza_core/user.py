import pydash as _
import yaml, os
from entity import Entity
from music_player import MusicPlayer
from alttime import AltTime
import logging

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
	#print self.time, type(self.time)
        try:    
            if not self.time:
                print "Not self.time"
                self.time = []
        except:
            self.time = []
        self.time.append(detected_time)

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

