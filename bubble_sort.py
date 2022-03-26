import time

start_time = time.time()


def bublesort(lst):
    swapped = True
    while swapped:
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = False


test = [0, 0, 0, 1, 4, 6, 4, 5, 6, 4235, 654, 543, 543, 65, 765, 4, 23, 654, 5, 436, 54, 543, 756, 65, 54, 432, 654,
        543, 765,
        876, 5243, ]

bublesort(test)

print(*test)

print("--- %s seconds ---" % (time.time() - start_time))
