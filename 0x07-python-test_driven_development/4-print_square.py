#!/usr/bin/python3
""" This module prints out a square with user-given size """


def print_square(size):
    """ This module safely prints out a square """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    # if no fail cases reached
    for row in range(0, size):
        print("{}".format('#' * size))
