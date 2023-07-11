#!/usr/bin/python3
"""this is file module"""


def write_file(filename="", text=""):
    """this is the func"""
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
