#!/usr/bin/python3
"""This creates a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This creates a square rectangle"""

    def __init__(self, size):
        super().__init__(size, size)
        self.__width = size
        self.__height = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__width, self.__height)
