import logging

logging.basicConfig(level=logging.INFO)
handler = logging.FileHandler('nalyzer_core.log')
handler.setLevel(logging.WARNING)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)

from .internet import Internet
from .music_player import MusicPlayer
from .process_runner import ProcessRunner

