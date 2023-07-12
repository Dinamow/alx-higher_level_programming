#!/usr/bin/python3
"""this is calss file"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """this if the calss"""
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return '[Square] {:d}/{:d}'.format(self.__size, self.__size)
