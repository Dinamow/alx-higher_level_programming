#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return None
    newone = my_list.copy()
    newone[idx] = element
    return newone
