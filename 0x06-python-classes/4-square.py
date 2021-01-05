#!/usr/bin/python3
"""This module creates a class to create a square"""


class Square:
    """This class creates a square and tests for failures"""
    def __init__(self, size=0):
        self.__size = size

    @property
    # This gets the size
    def size(self):
        return(self.__size)

    @size.setter
    # This sets the size
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
