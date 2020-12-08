#!/usr/bin/python3


def uppercase(str):
    for element in str:
        c = ord(element)
        if c >= 97 and c <= 122:
            c = ord(element) - 32
        print("{}".format(chr(c)), end='')

    print("")
