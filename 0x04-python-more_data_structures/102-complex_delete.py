#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    new = a_dictionary.copy()
    for i in a_dictionary:
        if a_dictionary[i] is value:
            del new[i]
    a_dictionary = new.copy()
    return a_dictionary
