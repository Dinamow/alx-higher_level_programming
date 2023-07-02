#!/usr/bin/python3
matrix = [
    [1, 2, 3, 4],
    [1, 2, 3, 4], 5
]
a = 'aaaa'

lenth = len(matrix)
for x in range(lenth):
    if not isinstance(matrix[x], list) or len(matrix[x]) == 0:  
        raise TypeError(a)
