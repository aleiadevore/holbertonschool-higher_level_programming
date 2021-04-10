#!/usr/bin/python3
""" Finds peak (larger than either side) in list """


def find_peak(list_of_integers):
        """ Finds peak in list """
        l = len(list_of_integers)
        ans = 0

        if l == 0:
                return None
        if l == 0:
                return list_of_integers[0]

        for i in range(1, l - 1):
                if list_of_integers[i] >= list_of_integers[i - 1] \
                        and list_of_integers[i] >= list_of_integers[i + 1]:
                        ans = list_of_integers[i]

        if ans == 0:
                if list_of_integers[0] >= list_of_integers[1]:
                        return list_of_integers[0]
                if list_of_integers[l - 1] >= list_of_integers[l - 2]:
                        return list_of_integers[l - 1]
        else:
                return ans
