#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for x in range(0, list_length):
        result = 0
        try:
            result = my_list_1[x] / my_list_2[x]
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            result_list.append(result)

    return result_list
