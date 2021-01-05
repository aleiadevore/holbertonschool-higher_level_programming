#!/usr/bin/python3
"""Creates a class to create a square"""


class Square:
    """This class creates a square and tests for failures"""
    def __init__(self, size=0):
        try:
            type(size) is int
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")
