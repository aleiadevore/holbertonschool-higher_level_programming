#!/usr/bin/python3
""" This creates a class that prevents the user from dynamically creating
new instances """


class LockedClass:
    """ This class prevents the user from dynamically creating
    new instances """
    __slots__ = ['first_name']
