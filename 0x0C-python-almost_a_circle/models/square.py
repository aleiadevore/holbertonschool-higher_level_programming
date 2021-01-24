#!/usr/bin/python3
"""This module creates a Square class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class inherits from Rectangle, which inherits from Base"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
