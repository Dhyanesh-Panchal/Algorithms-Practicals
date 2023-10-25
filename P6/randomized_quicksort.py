import numpy as np
import matplotlib.pyplot as plt

# Normal Quick sort
np.random.seed(10)


def partition(array, low, high):
    iterations = 0
    pivot = array[low]
    i = low + 1
    j = high

    while True:
        iterations += 1
        while i <= high and array[i] <= pivot:
            iterations += 1
            i += 1
        while j >= low and array[j] > pivot:
            iterations += 1
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]
        else:
            break

    array[low], array[j] = array[j], array[low]
    return j, iterations


def quicksort(array, low, high):
    iterations = 0
    if low < high:
        pivot_index, partitions_iteration = partition(array, low, high)
        iterations += partitions_iteration
        iterations += quicksort(array, low, pivot_index - 1)["iterations"]
        iterations += quicksort(array, pivot_index + 1, high)["iterations"]

    return {"array": array, "iterations": iterations}


# Randomized quicksort
def randomized_partition(array, low, high):
    iterations = 0
    pivot_index = np.random.randint(low, high)
    array[low], array[pivot_index] = array[pivot_index], array[low]

    pivot = array[low]
    i = low + 1
    j = high

    while True:
        iterations += 1
        while i <= high and array[i] <= pivot:
            iterations += 1
            i += 1
        while j >= low and array[j] > pivot:
            iterations += 1
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]
        else:
            break

    array[low], array[j] = array[j], array[low]
    return j, iterations


def randomized_quicksort(array, low, high):
    iterations = 0
    if low < high:
        pivot_index, partitions_iteration = randomized_partition(
            array, low, high)
        iterations += partitions_iteration
        iterations += randomized_quicksort(array,
                                           low, pivot_index - 1)["iterations"]
        iterations += randomized_quicksort(array,
                                           pivot_index + 1, high)["iterations"]

    return {"array": array, "iterations": iterations}


randomizedQuickSortMetadata = {"Random_Data": [],
                               "Ascending_data": [], "Descending_Data": []}
quickSortMetadata = {"Random_Data": [],
                     "Ascending_data": [], "Descending_Data": []}

for i in range(1000, 5001, 1000):

    # Random Data
    array = np.random.randint(0, i, i)
    randomizedQuickSortMetadata["Random_Data"].append(
        randomized_quicksort(array, 0, len(array) - 1))

    array = np.random.randint(0, i, i)
    quickSortMetadata["Random_Data"].append(
        quicksort(array, 0, len(array) - 1))

    # ascending and descending data
    # for normal quick sort it is exceeding my stack size (so not included).
    array = np.arange(0, i)
    randomizedQuickSortMetadata["Ascending_data"].append(
        randomized_quicksort(array, 0, len(array) - 1))
    array = list(range(0, i))
    array.reverse()
    randomizedQuickSortMetadata["Descending_Data"].append(
        randomized_quicksort(array, 0, len(array) - 1))

# print(randomizedQuickSortMetadata)

print(list(map(lambda x: x["iterations"],
               randomizedQuickSortMetadata["Descending_Data"])))

# print(list(map(lambda x: x["iterations"],
#    quickSortMetadata["Random_Data"])))


# randomizedQuickSort_iterationsList = list(
#     map(lambda x: x['iterations'], randomizedQuickSortMetadata["Random_Data"]))
# quickSort_iterationsList = list(
#     map(lambda x: x['iterations'], quickSortMetadata["Random_Data"]))


# plt.plot(randomizedQuickSort_iterationsList)
# plt.plot(quickSort_iterationsList)
# plt.legend(["randomized quick sort", "quick sort"])

# plt.show()
