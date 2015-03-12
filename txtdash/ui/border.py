# -*- coding: utf-8 -*-

import locale

locale.setlocale(locale.LC_ALL, '')


class Border(object):
    DEFAULT = []
    NONE = ['.', '.', '.', '.', '.', '.', '.', '.']
    THICK = ['@', '@', '@', '@', '@', '@', '@', '@']
    THIN = ['+', '+', '+', '+', '+', '+', '+', '+']
