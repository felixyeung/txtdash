from time import sleep
from _curses import error as CursesError


class Dash(object):
    def __init__(self, refresh=1):
        self.layout = set()
        self.boxes = set()
        self.refresh = refresh

    def bind(self, object):
        pass

    def show_forever(self):
        while True:
            try:
                sleep(self.refresh)
            except CursesError:
                # Our library should have handled everything that curses would cry about.
                pass