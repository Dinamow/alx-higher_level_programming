#!/usr/bin/python3
"""this is class file"""


class Square:
    """here the square class"""
    def __init__(self, size=0):
        """
        this descripe size

        Args:
            self: self arg
            size: size arg

        Return:
            nothing
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
