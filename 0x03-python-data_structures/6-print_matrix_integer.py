#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == None:
        return None
    limit = 1
    i = len(matrix) - 1
    for x in matrix:
        for a in x:
            if limit == i:
                print ("{:d}".format(a), end='')
            else:
                print ("{:d}".format(a), end=' ')
            limit += 1
        print()
        limit = 1
