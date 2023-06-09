#!/usr/bin/python3
"""this file for classse"""


class Rectangle(object):
    """this is rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        if not isinstance(width, int) or isinstance(width, bool):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if not isinstance(height, int) or isinstance(height, bool):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        a = self.print_symbol
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            return (a*self.__width+'\n')*(self.__height-1)+(a*self.__width)

    def __repr__(self):
        return 'Rectangle('+str(self.__width)+', '+str(self.__height)+')'

    def __del__(self):
        print('Bye rectangle...')
        type(self).number_of_instances -= 1

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
