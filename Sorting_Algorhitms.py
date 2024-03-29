import random
import time
import csv
import copy

def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]

        left = [x for x in array[1:] if x < pivot]
        right = [x for x in array[1:] if x >= pivot]

        return quicksort(left) + [pivot] + quicksort(right)


def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
        return array


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


def built_in_timsort(array):
    array.sort()
    return array


def main():

    dict_of_methods = {
        "Quicksort": quicksort,
        "Merge Sort": merge_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Bubble Sort": bubble_sort,
        "Timsort": built_in_timsort
    }


    number_of_elements = int(input("\n_______________________ \nInput a non-negative value as the number \nof elements in the generated array: "))
    if number_of_elements < 0:
        print("\n_______________________ \nThe number of elements must be POSITIVE. \nPlease TRY AGAIN")
        exit(1)

    integer_limits = int(input("\n_______________________ \nInput the limit for the integer values \nof random elements in the array: "))
    if integer_limits < 0:
        print("\nThe limit for the values must be POSITIVE. \n_______________________ \nPlease TRY AGAIN")
        exit(1)


    def generateArray(num_of_elements, int_limits):
        array_to_return = []
        if num_of_elements == 1:
            array_to_return.append(random.randint(-int_limits, int_limits))
        else:
            for i in range(num_of_elements):
                array_to_return.append(random.randint(-int_limits, int_limits))

        return array_to_return

    def measureTime():
        generated_array = generateArray(number_of_elements, integer_limits)
        dict_of_times = {}

        for method, sort_func in dict_of_methods.items():
            aux_array = copy.deepcopy(generated_array)
            start_time = time.time()
            sort_func(aux_array)
            end_time = time.time()
            dict_of_times[method] = end_time - start_time

        return dict_of_times


    def createCSV():
        sorted_list = sorted(measureTime().items(), key=lambda x: x[1])
        header = ["Method", "Execution Time"]
        items_for_file = []
        for i in sorted_list:
            aux_list = [i[0], str(i[1])]
            items_for_file.append(aux_list)
        with open("ResultFile.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(items_for_file)

    createCSV()

if __name__ == '__main__':
    main()

