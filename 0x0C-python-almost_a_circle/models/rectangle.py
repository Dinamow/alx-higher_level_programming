#!/usr/bin/python3
"""Define a Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Define a Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initiate values of Rectangle"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """access width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """change width value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """access height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """change width value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """access x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """change x's value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """access y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y's value"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area of Rect"""
        return self.__width * self.__height

    def display(self):
        """Display rectangle"""
        print("\n" * self.__y, end="")
        for x in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """print class as value"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y}\
 - {self.__width}/{self.__height}"

    def to_dictionary(self):
        """Return a dictionary"""
        return {'x': self.__x,
                'y': self.__y,
                'id': self.id,
                'height': self.__height,
                'width': self.__width}

    def update(self, *args, **kwargs):
        """Update rect"""
        if args:
            self.id = args[0] if len(args) > 0 else self.id
            if len(args) > 1:
                if type(args[1]) is not int:
                    raise TypeError("width must be an integer")
                elif args[1] <= 0:
                    raise ValueError("width must be > 0")
            self.__width = args[1] if len(args) > 1 else self.__width
            if len(args) > 2:
                if type(args[2]) is not int:
                    raise TypeError("height must be an integer")
                elif args[2] <= 0:
                    raise ValueError("height must be > 0")
            self.__height = args[2] if len(args) > 2 else self.__height
            if len(args) > 3:
                if type(args[3]) is not int:
                    raise TypeError("x must be an integer")
                elif args[3] < 0:
                    raise ValueError("x must be >= 0")
            self.__x = args[3] if len(args) > 3 else self.__x
            if len(args) > 4:
                if type(args[4]) is not int:
                    raise TypeError("y must be an integer")
                elif args[4] < 0:
                    raise ValueError("y must be >= 0")
            self.__y = args[4] if len(args) > 4 else self.__y
        elif kwargs:
            self.id = kwargs["id"] if "id" in kwargs else self.id
            if "width" in kwargs:
                if type(kwargs["width"]) is not int:
                    raise TypeError("width must be an integer")
                elif kwargs["width"] <= 0:
                    raise ValueError("width must be > 0")
                self.__width = kwargs["width"]
            if "height" in kwargs:
                if type(kwargs["height"]) is not int:
                    raise TypeError("height must be an integer")
                elif kwargs["height"] <= 0:
                    raise ValueError("height must be > 0")
                self.__height = kwargs["height"]
            if "x" in kwargs:
                if type(kwargs["x"]) is not int:
                    raise TypeError("x must be an integer")
                elif kwargs["x"] < 0:
                    raise ValueError("x must be >= 0")
                self.__x = kwargs["x"]
            if "y" in kwargs:
                if type(kwargs["x"]) is not int:
                    raise TypeError("y must be an integer")
                elif kwargs["y"] < 0:
                    raise ValueError("y must be >= 0")
                self.__y = kwargs["y"]
