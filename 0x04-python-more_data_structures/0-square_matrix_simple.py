#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    i, j = 0, 0
    new_matrix = matrix.copy()
    print(len(matrix))
    for x in new_matrix:
        for y in x:
            new_matrix[i][j] = y ** 2
            j += 1
        j = 0
        i += 1
    return new_matrix
