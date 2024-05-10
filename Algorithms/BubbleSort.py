def bubble_sort(array):
    if len(array) <= 1:
        return array
    else:
        n = len(array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array


# Test algorithm
array = [12, -5, 3, 0, 11, 0, -32, -15]
print("Sorted array:")
print(bubble_sort(array))