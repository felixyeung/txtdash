from txtdash.ui.arrangement import Arrangement
from txtdash.ui.border import Border
from txtdash.ui.utils import inner


class Layout(object):
    def __init__(self, root_box, padding=1, arrangement=Arrangement.HORIZONTAL):
        self.root = root_box
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
            self.padding = 0
        else:
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
        self.add_boxes(box)

    def arrange(self):
        n = len(self.boxes)
        method_name = '_arrange_{0}'.format(self.arrangement)
        getattr(self, method_name)(n)

    def _arrange_horizontal(self, n):
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

    def draw(self):
        self.root.border(Border.DOUBLE)
        self.root.draw()
        for box in list(self.boxes):
            box.border(Border.DEFAULT)
            box.draw()