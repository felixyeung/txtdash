import locale
from curses import panel
import curses

from txtdash.ui.utils import is_ascii


locale.setlocale(locale.LC_ALL, '')


class Box(object):
    def __init__(self, window=None):
        if window is not None:
            self.window = window
        else:
            self.window = curses.newwin(1, 1)
        self.panel = panel.new_panel(self.window)
        self.border = None

    def set_border(self, border_type):
        self.border = border_type
        return self

    def set_origin(self, top, left):
        self.window.mvwin(top, left)
        return self

    def set_dim(self, height, width):
        self.window.resize(height, width)
        return self

    def get_origin(self):
        return self.window.getbegyx()

    def get_dim(self):
        return self.window.getmaxyx()

    def draw(self):
        def draw_border(box):
            if is_ascii(''.join(box.border)):
                box.window.border(*box.border)
            else:
                h, w = box.get_dim()
                try:
                    for i in range(1, h - 1):
                        box.window.addstr(i, 0, box.border[0])
                        box.window.addstr(i, w - 1, box.border[1])
                    for i in range(1, w - 1):
                        box.window.addstr(0, i, box.border[2])
                        box.window.addstr(h - 1, i, box.border[3])
                    box.window.addstr(0, 0, box.border[4])
                    box.window.addstr(0, w - 1, box.border[5])
                    box.window.addstr(h - 1, 0, box.border[6])
                    box.window.addstr(h - 1, w - 1, box.border[7])
                except:
                    pass

        draw_border(self)
        self.window.refresh()


def make_boxes(n):
    return [Box() for each in range(n)]


def apply_border(border_type, boxes):
    for box in boxes:
        box.set_border(border_type)