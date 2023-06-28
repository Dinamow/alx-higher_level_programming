#!/usr/bin/python3
"""this is class file"""


class Square:
    """this is square class"""
    def __init__(self, size=0):
        """
        this define the size

        Args:
            self: self arg
            size: square size

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
         gets the area of square

         Args:
            self: self arg

        Return:
            the area of square
        """
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
