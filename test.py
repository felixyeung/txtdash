# -*- coding: utf-8 -*-

import curses as cs
from time import sleep
from txtdash.ui.arrangement import Arrangement
from txtdash.ui.border import Border
from txtdash.ui.box import Box
from txtdash.ui.layout import Layout
from txtdash.ui.utils import make_boxes


def foo(screen):
    cs.start_color()
    cs.curs_set(0)

    my_screen = Box(screen)
    my_layout = Layout(my_screen)

    my_boxes = make_boxes(Box, 5)

    my_layout.add_boxes(*my_boxes)
    my_layout.arrange()
    my_layout.draw()

    my_nested_boxes = make_boxes(Box, 3)
    my_second_layout = Layout(my_boxes[1], arrangement=Arrangement.VERTICAL).set_collapsed()
    my_second_layout.add_boxes(*my_nested_boxes)
    my_second_layout.arrange()
    my_second_layout.draw()

    my_nested_boxes_2 = make_boxes(Box, 7)
    my_second_layout = Layout(my_boxes[3], arrangement=Arrangement.VERTICAL)
    my_second_layout.add_boxes(*my_nested_boxes_2)
    my_second_layout.arrange()
    my_second_layout.draw()

    my_box = Box(cs.newwin(10, 20, 20, 20))
    my_box.border(Border.DEFAULT)
    c1 = cs.init_pair(1, cs.COLOR_RED, cs.COLOR_WHITE)
    c1 = cs.init_pair(2, cs.COLOR_YELLOW, cs.COLOR_BLUE)
    c1 = cs.init_pair(3, cs.COLOR_BLACK, cs.COLOR_GREEN)
    my_box.window.addstr(1, 1, 'hi world!', cs.color_pair(2))
    my_box.window.addstr(3, 1, 'bye world!', cs.color_pair(3))
    my_box.draw()

    while True:
        sleep(0.1)


cs.wrapper(foo)
