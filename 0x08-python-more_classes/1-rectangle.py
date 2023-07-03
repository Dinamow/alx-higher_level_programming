#!/usr/bin/python3
"""this file for classse"""


class Rectangle(object):
    """this is rectangle class"""
    def __init__(self, width=0, height=0):
        try:
            self.__width = int(width)
            if self.__width < 0:
                raise ValueError('width must be >= 0')
        except TypeError:
            raise TypeError('width must be an integer')
        try:
            self.__height = int(height)
            if self.__height < 0:
                raise ValueError('height must be >= 0')
        except TypeError:
            raise TypeError('height must be an integer')

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
