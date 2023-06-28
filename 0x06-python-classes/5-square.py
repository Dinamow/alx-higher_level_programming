#!/usr/bin/python3
"""this is calsses file"""


class Square:
    """this is square calll"""

    def __init__(self, size=0):
        """"
        this for size

        Args:
            self: self arg
            size: size atg

        Return: nothing
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
