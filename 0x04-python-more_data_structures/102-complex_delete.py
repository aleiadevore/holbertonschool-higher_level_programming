#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    new = a_dictionary.copy()
    for i in new:
        if new[i] is value:
            del a_dictionary[i]
    return a_dictionary
