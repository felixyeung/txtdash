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
    myscreen = Box(screen)
    myscreen.border(Border.THIN)

    mybox = Box(cs.newwin(10, 10, 20, 20))
    mybox.border(Border.THICK)

    myscreen.window.addstr(1, 1, 'what!')
    mybox.window.addstr(1, 1, 'hi world')
    
    myscreen.draw()
    mybox.draw()

    while True:
        pass

cs.wrapper(foo)
