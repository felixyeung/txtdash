# -*- coding: utf-8 -*-

import locale

locale.setlocale(locale.LC_ALL, '')


class Border(object):
    #TYPE = [ls, rs, ts, bs, tl, tr, bl, br]
    DEFAULT = ['│', '│', '─', '─', '┌', '┐', '└', '┘']
    DOUBLE = ['║', '║', '═', '═', '╔', '╗', '╚', '╝']
    NONE = ['.', '.', '.', '.', '.', '.', '.', '.']
    THICK = ['┃', '┃', '━', '━', '┏', '┓', '┗', '┛']
    DOTTED = ['┊', '┊', '┈', '┈', '┌', '┐', '└', '┘']
