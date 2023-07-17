#!/usr/bin/python3
"""Define a Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square: define a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Define square attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """return size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        self.width = value
        self.height = value

    def __str__(self):
        """print object as string"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def to_dictionary(self):
        """return a dictionary"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}

    def update(self, *args, **kwargs):
        """Update an element"""
        if args:
            self.id = args[0] if len(args) > 0 else self.id
            if len(args) > 1:
                if type(args[1]) is not int:
                    raise TypeError("width must be an integer")
                elif args[1] <= 0:
                    raise ValueError("width must be > 0")
            self.size = args[1] if len(args) > 1 else self.size
            if len(args) > 2:
                if type(args[2]) is not int:
                    raise TypeError("x must be an integer")
                elif args[2] < 0:
                    raise ValueError("x must be >= 0")
            self.x = args[2] if len(args) > 2 else self.x
            if len(args) > 3:
                if type(args[3]) is not int:
                    raise TypeError("y must be an integer")
                elif args[3] < 0:
                    raise ValueError("y must be >= 0")
            self.y = args[3] if len(args) > 3 else self.y
        elif kwargs:
            self.id = kwargs["id"] if "id" in kwargs else self.id
            if "size" in kwargs:
                if type(kwargs["size"]) is not int:
                    raise TypeError("width must be an integer")
                elif kwargs["size"] <= 0:
                    raise ValueError("width must be > 0")
                self.size = kwargs["size"]
            if "x" in kwargs:
                if type(kwargs["x"]) is not int:
                    raise TypeError("x must be an integer")
                elif kwargs["x"] < 0:
                    raise ValueError("x must be >= 0")
                self.x = kwargs["x"]
            if "y" in kwargs:
                if type(kwargs["y"]) is not int:
                    raise TypeError("y must be an integer")
                elif kwargs["y"] < 0:
                    raise ValueError("y must be >= 0")
                self.y = kwargs["y"]
