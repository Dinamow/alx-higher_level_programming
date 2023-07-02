#!/usr/bin/python3
"""
this file for func

first matrix_divided
"""


def matrix_divided(matrix, div):
    """
    this is matrix func
    """
    a = 'matrix must be a matrix (list of lists) of integers/floats'
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    elif isinstance(div, bool):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if matrix == None or len(matrix) == 0:
        raise TypeError(a)
    for x in matrix:
        if not isinstance(x, list):
            raise TypeError(a)
        for y in x:
            if not isinstance(y, int) and not isinstance(y, float):
                raise TypeError(a)
            elif isinstance(y, bool):
                raise TypeError(a)
    lenth = len(matrix)
    for x in range(lenth):
        if not isinstance(matrix[x], list) or len(matrix[x]) == 0:
            raise TypeError(a)
        if len(matrix[0]) != len(matrix[x]):
            raise TypeError('Each row of the matrix must have the same size')
    new_matrix = []
    for x in range(lenth):
        new_matrix.append([])
        for y in matrix[x]:
            new_matrix[x].append(round(y / div, 2))

    return new_matrix
