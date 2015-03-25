# -*- coding: utf-8 -*-

def is_ascii(s):
    """
    Given a string, determine if it consist only of ascii chars
    >>> is_ascii('hello world')
    True
    >>> is_ascii('˙´¬¬ø∑ ∑ø®¬∂')
    False
    >>> is_ascii(''.join(['║', '║', '═', '═', '╔', '╗', '╚', '╝']))
    False

    """
    return all(ord(c) < 128 for c in s)


def inner(val, padding=1):
    """
    Get the inner dimension given an outer dimension and padding
    >>> inner(10)
    8
    >>> inner(10, 3)
    4
    >>> inner(0, 1)
    -2
    """
    return val - (padding * 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
