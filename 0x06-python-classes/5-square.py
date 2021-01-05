#!/usr/bin/python3
"""This module creates a class to create a square and print it"""


class Square:
    """This class creates a square, tests for failures, and then prints out
    the square"""
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

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                print("{}".format('#' * self.__size))
