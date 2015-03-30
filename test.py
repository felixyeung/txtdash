import curses as cs
from time import sleep
from txtdash.content.provider import FunctionContentProvider

from txtdash.ui.arrangement import Arrangement
from txtdash.ui.border import Border
from txtdash.ui.box import Box, make_boxes, apply_border
from txtdash.ui.layout import Layout

from txtdash.plugin import Loader, Registry

def foo(screen):
    cs.start_color()
    cs.curs_set(0)

    my_screen = Box(screen)
    my_screen.set_border(Border.DOUBLE)
    my_layout = Layout(my_screen)

    my_boxes = make_boxes(5)
    apply_border(Border.DEFAULT, my_boxes)
    my_layout.add_boxes(*my_boxes)
    my_layout.arrange()
    my_layout.draw()

    my_nested_boxes = make_boxes(3)
    apply_border(Border.THICK, my_nested_boxes)
    my_second_layout = Layout(my_boxes[1], arrangement=Arrangement.VERTICAL).set_collapsed(False)
    my_second_layout.add_boxes(*my_nested_boxes)
    my_second_layout.arrange()
    my_second_layout.draw()

    my_nested_boxes_2 = make_boxes(7)
    apply_border(Border.DEFAULT, my_nested_boxes_2)
    my_third_layout = Layout(my_boxes[3], arrangement=Arrangement.VERTICAL)
    my_third_layout.add_boxes(*my_nested_boxes_2)
    my_third_layout.arrange()
    my_third_layout.draw()

    my_box = Box(cs.newwin(10, 20, 20, 20))
    my_box.set_border(Border.DOTTED)
    c1 = cs.init_pair(1, cs.COLOR_RED, cs.COLOR_WHITE)
    c1 = cs.init_pair(2, cs.COLOR_YELLOW, cs.COLOR_BLUE)
    c1 = cs.init_pair(3, cs.COLOR_BLACK, cs.COLOR_GREEN)
    my_box.window.addstr(1, 1, 'hi world!', cs.color_pair(2))
    my_box.window.addstr(3, 1, 'bye world!', cs.color_pair(3))
    my_box.draw()

    Loader.load('plugins')
    random_plugin = Registry.get('RandomPlugin')
    rand_instance = random_plugin(Box, FunctionContentProvider, 1, 10000000)
    assert isinstance(rand_instance.box, Box)
    assert isinstance(rand_instance.content, FunctionContentProvider)
    # TODO: fix bug where draw fails without calling set_border() first
    rand_instance.box.set_dim(20, 20).set_origin(10, 50).set_border(Border.DOTTED)
    # TODO: move type conversion into Provider?
    rand_instance.box.window.addstr(1, 1, str(rand_instance.content.fetch()))
    rand_instance.box.draw()

    while True:
        # TODO: a more robust way to redraw.
        my_layout.arrange()
        my_second_layout.arrange()
        my_third_layout.arrange()

        my_layout.resize()
        my_second_layout.resize()
        my_third_layout.resize()

        rand_instance.box.window.addstr(1, 1, str(rand_instance.content.fetch()))
        rand_instance.box.draw()
        sleep(1)


cs.wrapper(foo)
