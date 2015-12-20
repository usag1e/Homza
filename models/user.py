# import pydash as _
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
    def get_all_with_mac_addresses(self, mac_addresses):
        all_users = super(User, self).get_all()
        filtered_users = _.collections.filter_(
            users,
            lambda user: any(
                one_mac for one_mac in self.mac_addresses if one_mac in mac_addresses
            )
        )
        return filtered_users

