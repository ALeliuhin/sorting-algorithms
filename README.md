# sorting-algorithms
------------------------
REQUIREMENTS
------------------------

Python v.3.12.0

module "time"

module "random"

module "csv"

------------------------
DOCUMENTATION
------------------------
1. The program comprises two classes: "class Array" and "class ArraySorter"
2. The class "Array" allows to create an instance, utilizing properties based on user-input data.
3. The data that the user inputs are: number of elements in the object array, limits for the integers in the array.
4. A randomly shuffled array is then created, combining the following methods upon the object: makeFullySorted, reverseArray, write_to_file, read_from_file.
5. The methods above allow to make different operations on the array, adapting it for specific tests. The methods are already called automatically in main.py .
6. Afterwards, user is required to choose from algorithms available in class ArraySorter, that particularly combines static sorting functions and auxiliary functions.
7. Once the user picks desired algorithms, the program will iteratively apply each sorting method upon the array of data.
8. Three empirical results: Execution time (Unsorted), Execution time (Sorted), Execution time (Reversed), will eventually be written in a CSV file "sorting-times.csv".
9. User can turn the data in visual representation using the following vizualizer: https://webutility.io/csv-to-chart-online
