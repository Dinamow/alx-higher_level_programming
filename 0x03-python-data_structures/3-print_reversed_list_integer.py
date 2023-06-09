#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lenth = len(my_list)
    while (lenth > 0):
        print("{:d}".format(my_list[lenth - 1]))
        lenth -= 1
