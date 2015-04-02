from time import sleep


class Dash(object):
    def __init__(self, refresh=1):
        self.layout = set()
        self.boxes = set()
        self.refresh = refresh

    def bind(self, object):


    def show_forever(self):
        while True:
            sleep(self.refresh)
