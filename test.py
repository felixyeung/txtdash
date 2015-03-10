import logging
import time
import curses as cs
from curses import panel
from time import sleep
from functools import partial

logging.basicConfig(filename='mylog', level=logging.DEBUG)

class Box(object):
    def __init__(self, window=None):
       if window is not None:
           self.window = window
       else:
           self.window = cs.newwin(1, 1)
       self.panel = panel.new_panel(self.window)

    def set_origin(self, top, left):
        logging.debug(self.window)
        logging.debug('move to {0}, {1}'.format(top, left))
        self.window.mvwin(top, left)

    def set_dim(self, height, width):
        self.window.resize(height, width)

    def get_origin(self):
        return self.window.getbegyx()

    def get_dim(self):
        return self.window.getmaxyx()

    def draw(self):
        self.window.refresh()

    def border(self, type):
        self.window.border(*type)


class Border(object):
    THICK = ['@', '@', '@', '@', '@', '@', '@', '@']
    THIN = ['+', '+', '+', '+', '+', '+', '+', '+']

class Layout(object):
    ARRANGE_VERT = 1
    ARRANGE_HORIZ = 2

    def __init__(self, root_box):
        self.root = root_box
        self.root.border(Border.THIN)
        self.height, self.width = self._measure()
        self.inner_height = self.height - 2
        self.inner_width = self.width - 2
        self.boxes = set()

    def set_arrangement(self, arrangement):
        self.arrangement = arrangement

    def add_boxes(self, *boxes):
        for box in boxes:
           self.boxes.add(box)

    def add_box(self, box):
        self.addBoxes(box)

    def _measure(self):
        return self.root.get_dim()

    def arrange(self):
        # Horizontal arragement for now.
        n = len(self.boxes)
        box_width = self.inner_width / n
        bl = list(self.boxes)
        for i in range(0, n):
            logging.debug(i)
            bl[i].set_dim(self.inner_height, box_width)
            bl[i].set_origin(1, box_width * i + i)
            bl[i].border(Border.THICK)

    def draw(self):
        self.root.draw()
        for box in list(self.boxes):
            box.draw()

def foo(screen):
    cs.start_color()
    cs.curs_set(0)

    myscreen = Box(screen)
    mylayout = Layout(myscreen)
    box_a = Box()
    box_b = Box()
    box_c = Box()
    mylayout.add_boxes(box_a, box_b, box_c)
    mylayout.arrange()
    mylayout.draw()

    myscreen.border(Border.THIN)

    mybox = Box(cs.newwin(10, 20, 20, 20))
    mybox.border(Border.THICK)

    c1 = cs.init_pair(1, cs.COLOR_RED, cs.COLOR_WHITE)
    c1 = cs.init_pair(2, cs.COLOR_YELLOW, cs.COLOR_BLUE)
    c1 = cs.init_pair(3, cs.COLOR_BLACK, cs.COLOR_GREEN)

    #myscreen.window.addstr(1, 1, 'what!', cs.color_pair(1))
    mybox.window.addstr(1, 1, 'hi world!', cs.color_pair(2))
    mybox.window.addstr(3, 1, 'bye world!', cs.color_pair(3))    
    
    #myscreen.draw()
    mybox.draw()

    while True:
        sleep(0.1)

cs.wrapper(foo)
