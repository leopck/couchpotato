import sys
sys.path.append("..")

from selenium.webdriver.common.keys import Keys
from player import Player

class Ffmovies(Player):
    def __init__(self, handle):
        super().__init__(handle)

    def __del__(self):
        super().__del__()