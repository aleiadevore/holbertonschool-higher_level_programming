#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list is None:
        return 0
    numer = 0
    divisor = 0
    for i in my_list:
        numer += (i[0] * i[1])
        divisor += i[1]
    return numer / divisor
