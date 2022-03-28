from run_sorting_algorithm import algo_runtime as time
from random import randint


def bubble_sort(lst):
    swapped = True
    while swapped:
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = False
        if swapped:
            break
    return lst


ARRAY_LENGTH = 10000

if __name__ == "__main__":
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    time(algorithm="bubble_sort", array=array)
