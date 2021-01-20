#!/usr/bin/python3
"""This creates a class to invert '==' and '!='"""


class MyInt(int):
    """This class inverts '==' and '!='"""

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if self.value == other:
            return False
        else:
            return True

    def __ne__(self, other):
        if self.value == other:
            return True
        else:
            return False
