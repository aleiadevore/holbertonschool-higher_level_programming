#!/usr/bin/python3


def print_list_integer(my_list=[]):
    output = ["{}".format(elem) for elem in my_list]
    size = len(output)
    for i in range(0, size):
        print("{}".format(output[i]))
