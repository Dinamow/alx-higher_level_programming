#!/usr/bin/python3
"""this is the function file"""


def find_peak(list_of_integers):
    """the function find the peek"""

    if list_of_integers is None or\
        len(list_of_integers) == 0 or\
            not isinstance(list_of_integers, list):
        return None

    x = 0
    for i in list_of_integers:
        x = i if i > x else x
    return x
