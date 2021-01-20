#!/usr/bin/python3
"""This creates a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This creates a square rectangle"""

    def __init__(self, size):
        super().__init__(size, size)
