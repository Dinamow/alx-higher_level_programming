#!/usr/bin/python3
"""
this file made for func

1 - say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    types my name is <the names>
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print('My name is {:s} {:s}'.format(first_name, last_name))
