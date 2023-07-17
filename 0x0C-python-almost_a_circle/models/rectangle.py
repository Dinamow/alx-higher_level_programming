#!/usr/bin/python3
"""this is the file"""
from models.base import Base


class Rectangle(Base):
    """this is the calss file"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """this is init func"""
        if id is None:
            type(self).__nb_num += 1
            self.id = type(self).__nb_num
        else:
            self.id = id
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if type(y) is not int:
            raise TypeError('y must be integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        if height <= 0:
            raise TypeError('height must be > 0')
        if x < 0:
            raise TypeError('x must be >= to 0')
        if y < 0:
            raise TypeError('y must be >= to 0')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            """this is getter func"""
            return self.__width

        @width.setter
        def width(self, value):
            """this is setter func"""
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """this is getter func"""
            return self.__height

        @height.setter
        def height(self, value):
            """this is setter func"""
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """this is getter func"""
            return self.__x

        @x.setter
        def x(self, value):
            """this is setter func"""
            if type(value) is not int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            """this is getter func"""
            return self.__y

        @y.setter
        def y(self, value):
            """this is setter func"""
            if type(value) is not int:
                raise TypeError("y must be an integer")
            elif value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
