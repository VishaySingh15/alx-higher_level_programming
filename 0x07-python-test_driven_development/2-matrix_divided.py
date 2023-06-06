#!/usr/bin/python3
"""

This module divides a matrix by n

"""


def matrix_divided(matrix, div):
    """
    This function divides a matrix by div
    """

    length = 0
    count = 0
    new_matrix = []
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
        if not count:
            length = len(row)
            count += 1
        elif length != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for num in row:
            if type(num) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
            else:
                new_row.append(round(num / div, 2))
        new_matrix.append(new_row)
    return new_matrix
