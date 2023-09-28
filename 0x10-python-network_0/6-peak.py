"""this is the function file"""


def find_peak(list_of_integers):
    """the function find the peek"""

    low = 0
    high = len(list_of_integers) - 1

    if low > high:
        return None

    def partition(array, low, high):
        """helper func"""

        pivot = array[high]

        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:

                i = i + 1

                (array[i], array[j]) = (array[j], array[i])

        (array[i + 1], array[high]) = (array[high], array[i + 1])

        return i + 1

    def quickSort(array, low, high):
        if low < high:

            pi = partition(array, low, high)

            quickSort(array, low, pi - 1)

            quickSort(array, pi + 1, high)
        return array

    list_of_integers = quickSort(list_of_integers, low, high)

    return list_of_integers[-1]
