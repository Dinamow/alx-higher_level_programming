#!/usr/bin/python3
"""
this file for functions

add_integer
"""


def add_integer(a, b=98):
    """
    adding 2 integers
    """
    if not isinstance(a, int) and not isinstance(a, float)\
            or isinstance(a, bool):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float)\
            or isinstance(b, bool):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
