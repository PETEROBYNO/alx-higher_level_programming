#!/usr/bin/python3
'''
A simple matrix module
'''


def matrix_divided(matrix, div):
    ''' A function that divides all elements of a matrix '''
    error_msg = 'matrix must be a matrix (list of lists) of integers/floats'
    if not all(
            isinstance(row, list) and all(
                isinstance(element, (int, float)) for element in row
                ) for row in matrix
            ):
        raise TypeError(error_msg)

    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    result_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        result_matrix.append(new_row)

    return result_matrix
