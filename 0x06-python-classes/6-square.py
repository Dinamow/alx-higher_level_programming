#!/usr/bin/python3
"""this is calsses file"""


class Square:
    """this is square calll"""

    def __init__(self, size=0, position=(0, 0)):
        """"
        this for size

        Args:
            self: self arg
            size: size atg
            position: tuple arg

        Return: nothing
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        if position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__size = int(size)
        self.__position = position

    def area(self):
        """
        gets the area of square

        Args:
            self: self arg

        Return:
            the area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        this is print func

        Args:
            self: arg

        Return:
            nothing
        """
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print()

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

    @property
    def position(self):
        self.__position = position

    @position.setter
    def position(self, value):
        if value[0] <= 0 or value[1] <= 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        new_tuple(value[0], value[1])
