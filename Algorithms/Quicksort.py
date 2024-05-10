def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quicksort(array, low, high):
    while low < high:
        pi = partition(array, low, high)

        if pi - low < high - pi:
            quicksort(array, low, pi - 1)
            low = pi + 1
        else:
            quicksort(array, pi + 1, high)
            high = pi - 1


# Test algorithm
array = [12, -5, 3, 0, 11, 0, -32, -15]
quicksort(array, 0, len(array) - 1)
print("Sorted array:")
print(array)