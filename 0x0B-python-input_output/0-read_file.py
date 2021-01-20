#!/usr/bin/python3
"""Creates a function that reads a text file"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout"""
    with open(filename, 'r') as f:
        for line in f:
            print(line, end='')
    f.closed
