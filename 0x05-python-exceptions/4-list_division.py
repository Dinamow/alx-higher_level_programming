#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    try:
        for i in range(list_length):
            try:
                new_list.append(float(my_list_1[i] / my_list_2[i]))
            except IndexError:
                print("out of range")
                new_list.append(0)
            except ZeroDivisionError:
                print("division by 0")
                new_list.append(0)
            except TypeError:
                print("wrong type")
                new_list.append(0)
    finally:
        return new_list
