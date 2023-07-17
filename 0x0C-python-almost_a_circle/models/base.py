#!/usr/bin/python3
"""this is calss file"""


class Base:
    """this is the calss"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id == None:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
