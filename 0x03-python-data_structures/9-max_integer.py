#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    x = my_list[0]
    for a in my_list:
        if a > x:
            x = a
    return x
