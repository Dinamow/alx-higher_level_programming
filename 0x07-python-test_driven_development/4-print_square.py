#!/usr/bin/python3
"""this file for func"""


def print_square(size):
    """
    prin square
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for x in range(size):
        for y in range(size):
            print('#', end="")
        print()
