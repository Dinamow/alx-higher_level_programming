#!/usr/bin/python3
"""this is the function file"""


def find_peak(list_of_integers):
    """the function find the peek"""

    low = 0
    high = len(list_of_integers) - 1

    if low > high:
        return None

    def merge(arr, less, m, r):
        n1 = m - less + 1
        n2 = r - m

        L = [0] * (n1)
        R = [0] * (n2)

        for i in range(0, n1):
            L[i] = arr[less + i]

        for j in range(0, n2):
            R[j] = arr[m + 1 + j]

        i = 0
        j = 0
        k = less

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def mergeSort(arr, less, r):
        """the sort alogrithm"""
        if less < r:

            m = less+(r-less)//2

            mergeSort(arr, less, m)
            mergeSort(arr, m+1, r)
            merge(arr, less, m, r)
        return arr

    list_of_integers = mergeSort(list_of_integers, low, high)

    return list_of_integers[-1]
