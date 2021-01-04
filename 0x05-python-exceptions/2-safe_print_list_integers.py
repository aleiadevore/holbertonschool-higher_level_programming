#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(0, x):
            if type(my_list[i]) is not int:
                continue
            print("{:d}".format(my_list[i]), end='')
            count += 1
        print()
        return count
    except:
        raise
        print("IndexError: list index out of range")
        return count
