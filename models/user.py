import pydash as _
import yaml, os
from . import Entity
from Homza import MusicPlayer

class User(Entity):
    _collection = 'home_users'

    def __init__(self, name, mac_addresses=[], image=None, song=None):
        if not name:
            raise Entity.ArgumentMissingException('User.name')
        self._id = name
        already_saved = super(User, self).get()
        if already_saved is not None:
            self = already_saved
        else:
            self.mac_addresses = mac_addresses
            if image:
                self.image = image
            if song:
                self.song = song
            self.create()
    
    def play_song():
        MusicPlayer(self.song).play_song()

    @classmethod
    def get_all_with_mac_addresses(klass, mac_addresses):
        all_users = super(klass, self).get_all()
        filtered_users = _.collections.filter_(
            users,
            lambda user: any(
                one_mac for one_mac in self.mac_addresses if one_mac in mac_addresses
            )
        )
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
                            user.name,
                            user.mac_addresses,
                            user.image,
                            user.song
                        )
                    )
                return users_list
        except Exception as e:
            raise e

