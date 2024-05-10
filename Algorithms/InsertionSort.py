def insertion_sort(array):
    if len(array) <= 1:
        return array
    else:
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        return array


# Test algorithm
array = [12, -5, 3, 0, 11, 0, -32, -15]
print("Sorted array:")
print(insertion_sort(array))