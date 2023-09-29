#!/usr/bin/python3
"""this is the function file"""


def find_peak(list_of_integers):
    """the function find the peek"""

    if list_of_integers is None or\
        len(list_of_integers) == 0 or\
            not isinstance(list_of_integers, list):
        return None
    list_of_integers.sort()

    return list_of_integers[-1]
