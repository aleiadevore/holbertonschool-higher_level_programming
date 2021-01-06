#!/usr/bin/python3
"""This module creates a class to create a square and print it"""


class Square:
    """This class creates a square, tests for failures, and then prints out
    the square"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    # This gets the size
    def size(self):
        return(self.__size)

    # This gets the position
    def position(self):
        return(self.__position)

    @size.setter
    # This sets the size
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    # This sets the position
    def position(self, value):
        if not value[0] or not value[1]:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value[:]

    # Public, returns area
    def area(self):
        return self.__size * self.__size

    # Public, prints square
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            set = self.__position[:]
            x = set[0]
            y = set[1]
            print("{}".format('\n' * y), end='')
            for i in range(0, self.__size):
                print("{}{}".format(' ' * x, '#' * self.__size))
