#!/usr/bin/python3
"""this is class file"""


class Square:
    """this is the suqare class"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = int(size)
    def area(self):
        return self.__size ** 2
