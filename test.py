# -*- coding: utf-8 -*-

import locale
import logging
import curses as cs
from curses import panel
from time import sleep

locale.setlocale(locale.LC_ALL, '')
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
        self.window.border(*type)

    def _real_border(self):
        y, x = self.get_origin()
        try:
            self.window.addstr(0, 0, '╔')
        except:
            pass


class Border(object):
    DEFAULT = []
    NONE = ['.', '.', '.', '.', '.', '.', '.', '.']
    THICK = ['@', '@', '@', '@', '@', '@', '@', '@']
    THIN = ['+', '+', '+', '+', '+', '+', '+', '+']

    def is_ascii(cls):
        return all(ord(c) < 128 for c in s)


def inner(val, padding=1):
    return val - (padding * 2)


class Arrangement(object):
    HORIZONTAL = 'horizontial'
    VERTICAL = 'vertical'


class Layout(object):
    def __init__(self, root_box, padding=1, arrangement=Arrangement.HORIZONTAL):
        self.root = root_box
        self.root.border(Border.DEFAULT)
        self.padding = padding
        self.height, self.width = self.root.get_dim()
        self.top, self.left = self.root.get_origin()
        self.set_collapsed(False)
        self.set_arrangement(arrangement)
        # TODO: Use an OrderedSet
        self.boxes = set()

    def set_collapsed(self, collapsed=True):
        self.collapsed = collapsed

        if self.collapsed:
            self.root.border(Border.NONE)
            self.padding = 0
        else:
            self.root.border(Border.DEFAULT)
            self.padding = 1

        self.inner_height = inner(self.height, self.padding)
        self.inner_width = inner(self.width, self.padding)
        return self

    def set_arrangement(self, arrangement):
        self.arrangement = arrangement
        return self

    def add_boxes(self, *boxes):
        for box in boxes:
            self.boxes.add(box)

    def add_box(self, box):
        self.addBoxes(box)

    def arrange(self):
        n = len(self.boxes)
        method_name = '_arrange_{0}'.format(self.arrangement)
        getattr(self, method_name)(n)

    def _arrange_horizontial(self, n):
        box_width = (self.inner_width) / n
        remainder = (self.inner_width) % n
        bl = list(self.boxes)

        origin_adjustment = 0
        for i in range(0, n):
            size_adjustment = 0
            has_remainder = i < remainder
            # Previous item be a box index, and its box must have received an adjustment
            adjusted = 0 <= i - 1 < remainder
            if has_remainder:
                size_adjustment = 1
            if adjusted:
                # BE CAREFUL! adjustment to origin is cumulative!
                origin_adjustment += 1
            self._arrange_box(bl[i],
                              0,
                              (box_width * i) + origin_adjustment,
                              self.inner_height,
                              box_width + size_adjustment)

    def _arrange_vertical(self, n):
        # TODO Refactor with horizontal!
        box_height = (self.inner_height) / n
        remainder = (self.inner_height) % n
        bl = list(self.boxes)

        origin_adjustment = 0
        for i in range(0, n):
            size_adjustment = 0
            has_remainder = i < remainder
            # Previous item be a box index, and its box must have received an adjustment
            adjusted = 0 <= i - 1 < remainder
            if has_remainder:
                size_adjustment = 1
            if adjusted:
                # BE CAREFUL! adjustment to origin is cumulative!
                origin_adjustment += 1
            self._arrange_box(bl[i],
                              (box_height * i) + origin_adjustment,
                              0,
                              box_height + size_adjustment,
                              self.inner_width)

    def _arrange_box(self, box, top, left, height, width):
        box.set_dim(height, width)
        box.set_origin(self.padding + self.top + top, self.padding + self.left + left)
        box.border(Border.DEFAULT)

    def draw(self):
        self.root._real_border()
        self.root.draw()
        for box in list(self.boxes):
            box._real_border()
            box.draw()


def make_boxes(n):
    return [Box() for each in range(n)]


def foo(screen):
    cs.start_color()
    cs.curs_set(0)

    myscreen = Box(screen)
    mylayout = Layout(myscreen)

    myboxes = make_boxes(5)

    mylayout.add_boxes(*myboxes)
    mylayout.arrange()
    mylayout.draw()

    mynestedboxes = make_boxes(3)
    mysecondlayout = Layout(myboxes[1], arrangement=Arrangement.VERTICAL).set_collapsed()
    mysecondlayout.add_boxes(*mynestedboxes)
    mysecondlayout.arrange()
    mysecondlayout.draw()

    mynestedboxes2 = make_boxes(7)
    mysecondlayout = Layout(myboxes[3], arrangement=Arrangement.VERTICAL)
    mysecondlayout.add_boxes(*mynestedboxes2)
    mysecondlayout.arrange()
    mysecondlayout.draw()

    mybox = Box(cs.newwin(10, 20, 20, 20))
    mybox.border(Border.DEFAULT)
    c1 = cs.init_pair(1, cs.COLOR_RED, cs.COLOR_WHITE)
    c1 = cs.init_pair(2, cs.COLOR_YELLOW, cs.COLOR_BLUE)
    c1 = cs.init_pair(3, cs.COLOR_BLACK, cs.COLOR_GREEN)
    mybox.window.addstr(1, 1, 'hi world!', cs.color_pair(2))
    mybox.window.addstr(3, 1, 'bye world!', cs.color_pair(3))
    mybox.draw()

    while True:
        sleep(0.1)


cs.wrapper(foo)
