#!/usr/bin/python3
"""this is func file"""


def read_file(filename=""):
    """this is the func"""
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
