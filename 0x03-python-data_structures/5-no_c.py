#!/usr/bin/python3


def no_c(my_string):
    list1 = []
    list1[:0] = my_string

    x = list1.count('c')
    for i in range(0, x):
        list1.remove('c')

    x = list1.count('C')
    for i in range(0, x):
        list1.remove('C')

    new_string = ''

    for i in range(0, len(list1)):
        new_string += list1[i]

    return (new_string)
