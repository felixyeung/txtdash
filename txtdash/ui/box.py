# -*- coding: utf-8 -*-

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
        self.window.refresh()

    def border(self, type):
        if is_ascii(''.join(type)):
            self.window.border(*type)
        else:
            self._extended_border(type)

    def _extended_border(self, type):
        y, x = self.get_origin()
        try:
            self.window.addstr(0, 0, type[0])
        except:
            pass