#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    x = 0
    y = 0
    if len(tuple_a) < 1:
        x += 0
    else:
        x += tuple_a[0]
    if len(tuple_b) < 1:
        x += 0
    else:
        x += tuple_b[0]
    if len(tuple_a) < 2:
        y += 0
    else:
        y += tuple_a[1]
    if len(tuple_b) < 2:
        y += 0
    else:
        y += tuple_b[1]
    new_tuple = (x, y)

    return (new_tuple)
