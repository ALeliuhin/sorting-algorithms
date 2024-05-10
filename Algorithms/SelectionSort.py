def selection_sort(array):
    if len(array) <= 1:
        return array
    else:
        for i in range(len(array)):
            min_index = i

            for j in range(i + 1, len(array)):
                if array[j] < array[min_index]:
                    min_index = j
            (array[i], array[min_index]) = (array[min_index], array[i])
        return array

# Test algorithm
array = [12, -5, 3, 0, 11, 0, -32, -15]
print("Sorted array:")
print(selection_sort(array))