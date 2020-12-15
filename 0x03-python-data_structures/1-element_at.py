#!/usr/bin/python3


def element_at(my_list, idx):
    size = len(my_list)

    if idx > size - 1:
        return (None)

    x = my_list[idx]

    if x < 0:
        return (None)
    return (x)
