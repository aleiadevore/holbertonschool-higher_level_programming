#!/usr/bin/python3
""" This module creates a class that defines and initializes rectangle and
returns the area and perimeter """


class Rectangle:
    """ This class defines and initializes a rectangle and returns
    the area and perimeter """
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    # This gets the width
    def width(self):
        return(self.__width)

    @width.setter
    # This sets the width
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    # This gets the height.
    def height(self):
        return(self.__height)

    @height.setter
    # This sets the height.
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # public, returns area
    def area(self):
        return self.__width * self.__height

    # public, returns perimeter
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * 2 + self.__width * 2
