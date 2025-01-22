#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = list(map(square, row))
        new_matrix.append(new_row)
    return new_matrix


def square(a):
    return a*a
