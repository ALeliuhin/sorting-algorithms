import random
import os
import time
import csv

class ArraySorter:
    @staticmethod
    def partition(array, low, high):
        pivot = array[high]
        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]

        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    @staticmethod
    def quicksort(array, low, high):
        while low < high:
            pi = ArraySorter.partition(array, low, high)

            if pi - low < high - pi:
                ArraySorter.quicksort(array, low, pi - 1)
                low = pi + 1
            else:
                ArraySorter.quicksort(array, pi + 1, high)
                high = pi - 1


    @staticmethod
    def merge_sort(array):
        if len(array) <= 1:
            return array
        else:
            mid = len(array) // 2
            left = array[:mid]
            right = array[mid:]

            ArraySorter.merge_sort(left)
            ArraySorter.merge_sort(right)

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

    @staticmethod
    def insertion(arr, left=0, right=None):
        if right is None:
            right = len(arr) - 1

        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    @staticmethod
    def merge(arr, l, m, r):
        len1, len2 = m - l + 1, r - m
        left, right = arr[l:m + 1], arr[m + 1:r + 1]

        i, j, k = 0, 0, l

        while i < len1 and j < len2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len1:
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len2:
            arr[k] = right[j]
            j += 1
            k += 1

    @staticmethod
    def timsort(array):
        min_run = 32
        n = len(array)

        for i in range(0, n, min_run):
            ArraySorter.insertion(array, i, min((i + min_run - 1), n - 1))

        size = min_run
        while size < n:
            for left in range(0, n, 2 * size):
                mid = left + size - 1
                right = min((left + 2 * size - 1), (n - 1))
                if mid < right:
                    ArraySorter.merge(array, left, mid, right)
            size *= 2

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def heapify(array, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and array[left] > array[largest]:
            largest = left

        if right < n and array[right] > array[largest]:
            largest = right

        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            ArraySorter.heapify(array, n, largest)

    @staticmethod
    def heap_sort(array):
        n = len(array)

        for i in range(n // 2 - 1, -1, -1):
            ArraySorter.heapify(array, n, i)
        for i in range(n - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            ArraySorter.heapify(array, i, 0)

        return array

class Array:
    def __init__(self, number_of_elements, numbers_margin):
        self.number_of_elements = number_of_elements
        self.numbers_margin = numbers_margin
        self.array = []
        for i in range(number_of_elements):
            self.array.append(random.randint(-numbers_margin, numbers_margin))

    def __str__(self):
        return ' '.join(map(str, self.array))

    def makeHalfSorted(self):
        half_index = self.number_of_elements // 2
        self.array[:half_index] = sorted(self.array[:half_index])

    def makeFullySorted(self):
        self.array.sort()

    def reverseArray(self):
        self.array.sort()
        self.array = self.array[::-1]

    def write_original_array(self, filename="original_array.txt"):
        with open(filename, 'w') as file:
            file.write(' '.join(map(str, self.array)))

    def read_original_array(self, filename="original_array.txt"):
        with open(filename, 'r') as file:
            self.array = list(map(int, file.read().split()))


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def makeArrayObject():
    number_of_elements = None
    numbers_margin = None

    print("\t\t=== Sorting Methods Comparison ===")

    bool_create_object = True

    while bool_create_object:
        number_of_elements = int(input("Input a positive number of integers to sort: "))
        if number_of_elements >= 0:
            bool_create_object = False
            break
        print("Invalid input data. Please try again.\n")

    bool_create_object = True
    while bool_create_object:
        numbers_margin = int(input("Input a positive integer limit for the elements of the array: "))
        if numbers_margin >= 0:
            bool_create_object = False
            break
        print("Invalid input data. Please try again.\n")

    array_object = Array(number_of_elements, numbers_margin)
    array_object.write_original_array()

    sorting_methods = {
        "1": ArraySorter.quicksort,
        "2": ArraySorter.merge_sort,
        "3": ArraySorter.selection_sort,
        "4": ArraySorter.insertion_sort,
        "5": ArraySorter.bubble_sort,
        "6": ArraySorter.heap_sort,
        "7": ArraySorter.timsort
    }

    csv_data = []

    choices = input(
        "\nChoose sorting methods (comma-separated): "
        "\n1. Quicksort"
        "\n2. Merge Sort"
        "\n3. Selection Sort"
        "\n4. Insertion Sort"
        "\n5. Bubble Sort"
        "\n6. Heap Sort"
        "\n7. Timsort"
        "\n\nEnter your choices (e.g., 1,3,5): ").split(
        ',')


    for choice in choices:
        if choice in sorting_methods:
            list_of_time = []
            print(f"\nSorted Array using {sorting_methods[choice].__name__}:")

            if choice == "1":
                # Unsorted
                start_time = time.time()
                sorting_methods[choice](array_object.array, 0, array_object.number_of_elements - 1)
                end_time = time.time()
                list_of_time.append(end_time - start_time)

                # Sorted
                start_time = time.time()
                sorting_methods[choice](array_object.array, 0, array_object.number_of_elements - 1)
                end_time = time.time()
                list_of_time.append(end_time - start_time)

                # Reversed
                array_object.reverseArray()
                start_time = time.time()
                sorting_methods[choice](array_object.array, 0, array_object.number_of_elements - 1)
                end_time = time.time()
                list_of_time.append(end_time - start_time)
            else:
                # Unsorted
                start_time = time.time()
                sorting_methods[choice](array_object.array)
                end_time = time.time()
                list_of_time.append(end_time - start_time)

                # Sorted
                start_time = time.time()
                sorting_methods[choice](array_object.array)
                end_time = time.time()
                list_of_time.append(end_time - start_time)

                # Reversed
                array_object.reverseArray()
                start_time = time.time()
                sorting_methods[choice](array_object.array)
                end_time = time.time()
                list_of_time.append(end_time - start_time)

            print(f"Execution time (Unsorted): {list_of_time[0]:.6f} seconds")
            print(f"Execution time (Sorted): {list_of_time[1]:.6f} seconds")
            print(f"Execution time (Reversed): {list_of_time[2]:.6f} seconds")
            array_object.read_original_array()
            # Collect data for CSV
            csv_data.append([sorting_methods[choice].__name__, list_of_time[0], list_of_time[1], list_of_time[2]])
        else:
            print(f"Invalid choice '{choice}'")

    # Write data to CSV file
    with open('sorting_times.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Time (Unsorted)', 'Time (Fully-sorted)', 'Time (Reversed)'])
        writer.writerows(csv_data)

    del array_object

def main():
    makeArrayObject()
    bool_main = True
    while bool_main:
        choice = input("\nDo you want to make another test? [y/N] : ")
        if choice == 'y':
            print("\n\n")
            makeArrayObject()
        else:
            bool_main = False
            print("Exiting...")


if __name__ == '__main__':
    main()



