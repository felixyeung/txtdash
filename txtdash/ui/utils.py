def is_ascii(s):
    return all(ord(c) < 128 for c in s)


def inner(val, padding=1):
    return val - (padding * 2)
