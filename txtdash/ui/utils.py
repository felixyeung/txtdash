def is_ascii(s):
    return all(ord(c) < 128 for c in s)


def inner(val, padding=1):
    return val - (padding * 2)


def make_boxes(box_cls, n):
    return [box_cls() for each in range(n)]
