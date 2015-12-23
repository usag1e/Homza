import logging

logging.basicConfig(level=logging.INFO)
handler = logging.FileHandler('homza.log')
handler.setLevel(logging.WARNING)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)

from .internet import Internet
from .music_player import MusicPlayer
from .process_runner import ProcessRunner
from .entity import Entity
from .house import House
from .alttime import AltTime
from .user import User
from .iss import IssFinder
from .network_sweeper import NetworkSweeper
from .weather import WeatherCenter
from .subway import Subway

House.init()
User.init()

