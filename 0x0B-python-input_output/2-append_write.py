#!/usr/bin/python3
"""this if func file"""


def append_write(filename="", text=""):
    """this is func"""
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
