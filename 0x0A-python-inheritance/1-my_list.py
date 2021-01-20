#!/usr/bin/python3
"""Creates a class MyList that inherits from list"""


class MyList(list):
    """This creates an inherited class that prints a sorted list"""

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        nlist = sorted(self)
        print(nlist)
