#!/usr/bin/python3
"""this is calss file"""
from models.base import Base


class Rectangle(Base):
    """this is the calss file"""
    __nb_num = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        if id is None:
            type(self).__nb_num += 1
            self.id = type(self).__nb_num
        else:
            self.id = id
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            return self.__width

        def height(self):
            return self.__height

        def x(self):
            return self.__x

        def y(self):
            return self.__y

        @width.setter
        def width(self, value):
            self.__width = value

        @height.setter
        def height(self, value):
            self.__height = value

        @x.setter
        def x(self, value):
            self.__x = value

        @y.setter
        def y(self, value):
            self.__y = value
