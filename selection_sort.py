from run_sorting_algorithm import algo_runtime as time
from random import randint


def selection_sort(arr):
    for i in range(len(arr) - 1):
        minimum = i
        for j in range(i + 1, len(arr) - 1):
            if arr[j] < arr[minimum]:
                minimum = j

        arr[minimum], arr[i] = arr[i], arr[minimum]


ARRAY_LENGTH = 1000

if __name__ == "__main__":
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    time(algorithm="selection_sort", array=array)


