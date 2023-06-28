#!/usr/bin/python3
"""this is class file"""


class Square:
    """this is the suqare class"""
    def __init__(self, size=0):
        """
        this gets the size
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
        self.__size = int(size)

    def area(self):
        """
        this gets the square area
        Args:
            self: self arg

        Return:
            area of the square
        """
        return self.__size ** 2
