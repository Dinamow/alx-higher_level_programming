#!/usr/bin/python3
"""this is calss file"""
from models.base import Base


class Rectangle(Base):
    """this is the calss file"""
    __nb_num = 0
    def __init__(self, width, height, x=0, y=0, id=None):
        if id == None:
            type(self).__nb_num += 1
            self.id = type(self).__nb_num
        else:
            self.id = id
