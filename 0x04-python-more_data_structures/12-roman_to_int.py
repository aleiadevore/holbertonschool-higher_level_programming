#!/usr/bin/python3


def roman_to_int(roman_string):
    sum = 0
    prev = None
    if roman_string is None or type(roman_string) is int:
        return 0
    for i in reversed(roman_string):
        if i == 'I':
            if prev is None or prev is 'I':
                sum += 1
            else:
                sum -= 1
        elif i == 'V':
            if prev is None or prev is 'I' or prev is 'V':
                sum += 5
            else:
                sum -= 5
        elif i == 'X':
            if prev is None or prev is 'I' or prev is 'V' or prev is 'X':
                sum += 10
            else:
                sum -= 10
        elif i == 'L':
            if (prev is None or prev is 'I' or prev is 'V' or prev is 'X' or
               prev is 'L'):
                sum += 50
            else:
                sum -= 50
        elif i == 'C':
            if (prev is None or prev is 'I' or prev is 'V' or prev is 'X' or
               prev is 'L' or prev is 'C'):
                sum += 100
            else:
                sum -= 100
        elif i == 'D':
            if prev is None or sum < 1000:
                sum += 500
            else:
                sum -= 500
        elif i == 'M':
            if (prev is None or prev is 'I' or prev is 'V' or prev is 'X' or
               prev is 'L' or prev is 'C' or prev is 'M'):
                sum += 1000
            else:
                sum -= 1000
        else:
            return 0
        prev = i
    return sum
