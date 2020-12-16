#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix]))
