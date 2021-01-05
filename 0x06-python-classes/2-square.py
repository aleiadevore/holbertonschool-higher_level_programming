#!/usr/bin/python3
"""Creates a class to create a square"""


class Square:
    """This class creates a square and tests for failures"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
