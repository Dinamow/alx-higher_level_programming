#!/usr/bin/python3
"""this is func file"""


def inherits_from(obj, a_class):
    """the func"""
    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)
