#!/usr/bin/python3
"""this is class file"""


class Square:
    """here the square class"""
    def __init__(self, size=0):
        try:
            int(size)
        except ValueError:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
