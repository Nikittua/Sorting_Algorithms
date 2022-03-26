import time

start_time = time.time()


def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j

        arr[minimum], arr[i] = arr[i], arr[minimum]


test = [0, 0, 0, 1, 4, 6, 4, 5, 6, 4235, 654, 543, 543, 65, 765, 4, 23, 654, 5, 436, 54, 543, 756, 65, 54, 432, 654,
        543, 765,
        876, 5243, ]

selection_sort(test)

print(*test)

print("--- %s seconds ---" % (time.time() - start_time))
