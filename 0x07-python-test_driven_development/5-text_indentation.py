#!/usr/bin/python3
""" This module prints two blank lines after '.', '?' and ':' """


def text_indentation(text):
    """This module adds blank lines after special characters"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for c in text:
        if c == ' ' and b == 1:
            continue
        if c == '.' or c == '?' or c == ':':
            print("{}{}".format(c, '\n'))
            b = 1
        else:
            print(c, end='')
            b = 0
