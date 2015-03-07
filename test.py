import time
import curses as cs
from curses import panel
from time import sleep
from functools import partial

class Box(object):
    def __init__(self, window=None):
       if window is not None:
           self.window = window
           self.panel = panel.new_panel(self.window)
    
    def draw(self):
        self.window.refresh()

    def border(self, type):
        self.window.border(*type)

class Border(object):
    THICK = ['@', '@', '@', '@', '@', '@', '@', '@']
    THIN = ['+', '+', '+', '+', '+', '+', '+', '+']

def foo(screen):
    cs.start_color()
    cs.curs_set(0)

    myscreen = Box(screen)
    myscreen.border(Border.THIN)

    mybox = Box(cs.newwin(10, 20, 20, 20))
    mybox.border(Border.THICK)

    c1 = cs.init_pair(1, cs.COLOR_RED, cs.COLOR_WHITE)
    c1 = cs.init_pair(2, cs.COLOR_YELLOW, cs.COLOR_BLUE)
    c1 = cs.init_pair(3, cs.COLOR_BLACK, cs.COLOR_GREEN)

    myscreen.window.addstr(1, 1, 'what!', cs.color_pair(1))
    mybox.window.addstr(1, 1, 'hi world!', cs.color_pair(2))
    mybox.window.addstr(3, 1, 'bye world!', cs.color_pair(3))    
    
    myscreen.draw()
    mybox.draw()

    while True:
        sleep(0.1)

cs.wrapper(foo)
