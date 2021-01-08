#!/usr/bin/python3
""" This module divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """ This module divides all elements of a matrix."""
    # fail cases
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    prevlen = len(matrix[0])
    for row in matrix:
        if len(row) != prevlen:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError(
                  "matrix must be a matrix (list of lists) of integers/floats")
        prevlen = len(row)

    # if no fail cases met
    newmatrix = []
    for row in matrix:
        newrow = []
        for elem in row:
            newrow.append(round(elem / div, 2))
        newmatrix.append(newrow)
    return newmatrix
