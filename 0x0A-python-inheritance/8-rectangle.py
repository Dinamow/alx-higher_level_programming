#!/usr/bin/python3
"""this is calss file"""


class BaseGeometry:
    """this if the calss"""
    def __init__(self, width, height):
        if type(width) is not int:
            raise TypeError('width must me integer')
        if width < 0:
            raise ValueError('width must be positive integer')
        if type(height) is not int:
            raise TypeError('height must me integer')
        if height < 0:
            raise ValueError('height must be positive integer')
        self.__width = width
        self.__height = height

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
