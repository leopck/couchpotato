class Player:
    def __init__(self, webcontrol):
        self.webcontrol = webcontrol

    def focusPlayer(self):
        raise NotImplementedError

    def pause(self):
        raise NotImplementedError

    def play(self):
        raise NotImplementedError

    def fullscreen(self):
        raise NotImplementedError

    def fastforward(self):
        raise NotImplementedError

    def rewind(self):
        raise NotImplementedError

    def volUp(self):
        raise NotImplementedError

    def volDown(self):
        raise NotImplementedError

    def loadVideo(self, url):
        raise NotImplementedError

    def nextVideo(self):
        raise NotImplementedError

    def previousVideo(self):
        raise NotImplementedError

    def searchVideo(self, search):
        raise NotImplementedError