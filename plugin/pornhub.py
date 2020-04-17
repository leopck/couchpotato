import sys
sys.path.append("..")

from selenium.webdriver.common.keys import Keys
from player import Player

class Pornhub(Player):
    def __init__(self, webcontrol):
        super().__init__(webcontrol)

    def focusPlayer(self):
        self.element = self.webcontrol.driver.switch_to_active_element()
        # self.element = self.webcontrol.driver.find_element_by_tag_name("video-element")
        return self.element

    def pause(self):
        import pdb; pdb.set_trace()
        self.element = self.focusPlayer()
        self.webcontrol.sendKey(self.element, Keys.SPACE)
        return "Success"

    def play(self):
        self.element = self.focusPlayer()
        self.webcontrol.sendKey(self.element, Keys.SPACE)
        return "Success"

    def fullscreen(self):
        self.element = self.focusPlayer()
        self.webcontrol.sendKey(self.element, "F")
        return "Success"

    def fastforward(self):
        self.element = self.focusPlayer()
        self.webcontrol.sendKey(self.element, Keys.RIGHT)
        return "Success"

    def rewind(self):
        self.element = self.focusPlayer()
        self.webcontrol.sendKey(self.element, Keys.LEFT)
        return "Success"

    def volUp(self):
        self.element = self.focusPlayer()
        self.webcontrol.sendKey(self.element, Keys.UP)
        return "Success"

    def volDown(self):
        self.element = self.focusPlayer()
        self.webcontrol.sendKey(self.element, Keys.DOWN)
        return "Success"

    def loadVideo(self, url):
        self.go(url)
        return "Success"

    def nextVideo(self):
        raise NotImplementedError

    def previousVideo(self):
        raise NotImplementedError

    def searchVideo(self, search):
        raise NotImplementedError