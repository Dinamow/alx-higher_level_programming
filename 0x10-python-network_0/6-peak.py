#!/usr/bin/python3
"""this is the function file"""


def find_peak(list_of_integers):
    """the function find the peek"""

    if not isinstance(list_of_integers, list):
        return None

    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    length = len(list_of_integers)

    if length == 1:
        return list_of_integers[0]

    if length == 2:
        return list_of_integers[0] if list_of_integers[0] >\
            list_of_integers[1] else list_of_integers[1]

    def get_value(arr: list, index: int):
        """get index value"""

        x = []
        if index == len(arr) - 1:
            if arr[index] > arr[index - 1]:
                x.append(arr[index])
                return x
            else:
                x.append(arr[index - 1])
                return x

        x.append(arr[index])

        if x[0] < arr[index - 1]:
            x[0] = arr[index - 1]
        elif x[0] < arr[index + 1]:
            x[0] = arr[index + 1]

        return x

    x = get_value(list_of_integers, 1)

    if length == 3:
        return x[0]

    new = x

    for i in range(4, length - 1, 3):
        new.append(get_value(list_of_integers, i)[0])

    if length % 3 != 0:
        new.append(list_of_integers[length - 1])

    return (find_peak(new))
