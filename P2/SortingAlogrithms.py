import time as T
import numpy as np
import matplotlib.pyplot as plt


def selectionSort(arr):
    newarray = arr[::]
    # startTime = T.time_ns()
    iterations = 0

    for (i, ele) in enumerate(newarray):
        minIndx = i
        for j in range(i+1, len(newarray)):
            iterations += 1
            if newarray[j] < newarray[minIndx]:
                minIndx = j

        newarray[i], newarray[minIndx] = newarray[minIndx], newarray[i]

    # endTime = T.time_ns()
    return newarray, iterations


def bubbleSort(arr):
    newarray = arr[::]
    iterations = 0

    n = len(newarray)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            iterations += 1
            if newarray[j] > newarray[j + 1]:
                newarray[j], newarray[j + 1] = newarray[j + 1], newarray[j]
                swapped = True

        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break

    return {"array": newarray, "interations": iterations}


def insertionSort(arr):
    newarray = arr[::]
    iterations = 0

    for i in range(1, len(newarray)):
        key = newarray[i]
        j = i - 1
        iterations += 1
        while j >= 0 and key < newarray[j]:
            newarray[j + 1] = newarray[j]
            j -= 1
            iterations += 1
        newarray[j + 1] = key

    return {"array": newarray, "iterations": iterations}


def mergeSort(arr):
    iterations = 0
    if len(arr) <= 1:
        iterations += 1
        return {"array": arr, "iterations": iterations}

    # Divide the array into two halves
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    iterations += (left['iterations'] + right['iterations'])

    # Merge the two sorted halves
    merged = merge(left["array"], right["array"])
    iterations += merged['iterations']
    return {"array": merged['array'], "iterations": iterations}


def merge(left, right):
    iterations = 0
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        iterations += 1
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add any remaining elements from the left or right arrays
    merged.extend(left[i:])
    merged.extend(right[j:])
    iterations += (len(left[i:]) + len(right[j:]))

    return {"array": merged, "iterations": iterations}


def quickSort(arr):

    try:

        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            iterations = 0

            for j in range(low, high):
                iterations += 1
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1, iterations

        def quickSortHelper(arr, low, high):
            iterations = 0

            if low < high:
                partitionIndex, partitionIterations = partition(arr, low, high)
                iterations += partitionIterations

                iterations += quickSortHelper(arr, low, partitionIndex - 1)
                iterations += quickSortHelper(arr, partitionIndex + 1, high)

            return iterations

        newarray = arr[::]
        print(len(newarray))
        iterations = quickSortHelper(newarray, 0, len(newarray) - 1)
        return {"array": newarray, "iterations": iterations}
    except RecursionError as e:
        return {"error": e, "array": arr}


if __name__ == '__main__':
    # arr = list(map(int,input("Enter the array").split(' ')))
    selectionSortMetadata = {"Random_Data": [],
                             "Ascending_data": [], "Descending_Data": []}
    bubbleSortMetadata = {"Random_Data": [],
                          "Ascending_data": [], "Descending_Data": []}
    insertionSortMetadata = {"Random_Data": [],
                             "Ascending_data": [], "Descending_Data": []}
    quickSortMetadata = {"Random_Data": [],
                         "Ascending_data": [], "Descending_Data": []}
    mergeSortMetadata = {"Random_Data": [],
                         "Ascending_data": [], "Descending_Data": []}

    np.random.seed(10)
    # Random Order Data
    for i in range(1000, 5001, 1000):
        arr = np.random.randint(0, i, i)
        selectionSortMetadata["Random_Data"].append(selectionSort(arr))
        arr = np.random.randint(0, i, i)
        bubbleSortMetadata["Random_Data"].append(bubbleSort(arr))
        arr = np.random.randint(0, i, i)
        insertionSortMetadata["Random_Data"].append(insertionSort(arr))
        arr = np.random.randint(0, i, i)
        mergeSortMetadata["Random_Data"].append(mergeSort(arr))
        arr = np.random.randint(0, i, i)
        quickSortMetadata["Random_Data"].append(quickSort(arr))

    # Descending Order Data
    for i in range(1000, 5001, 1000):
        arr = list(range(i))
        arr.reverse()
        selectionSortMetadata["Ascending_data"].append(selectionSort(arr))
        arr = list(range(i))
        arr.reverse()
        bubbleSortMetadata["Ascending_data"].append(bubbleSort(arr))
        arr = list(range(i))
        arr.reverse()
        insertionSortMetadata["Ascending_data"].append(insertionSort(arr))
        arr = list(range(i))
        arr.reverse()
        mergeSortMetadata["Ascending_data"].append(mergeSort(arr))
        arr = list(range(i))
        arr.reverse()
        quickSortMetadata["Ascending_data"].append(quickSort(arr))

    # Ascending Order Data
    for i in range(1000, 5001, 1000):
        arr = list(range(i))
        selectionSortMetadata["Ascending_data"].append(selectionSort(arr))
        arr = list(range(i))
        bubbleSortMetadata["Ascending_data"].append(bubbleSort(arr))
        arr = list(range(i))
        insertionSortMetadata["Ascending_data"].append(insertionSort(arr))
        arr = list(range(i))
        mergeSortMetadata["Ascending_data"].append(mergeSort(arr))
        arr = list(range(i))
        quickSortMetadata["Ascending_data"].append(quickSort(arr))

    print(selectionSortMetadata)
    print(bubbleSortMetadata)
    print(insertionSortMetadata)
    print(mergeSortMetadata)
    print(quickSortMetadata)

    # iterationsList = list(
    #     map(lambda x: x['iterations'], selectionSortMetadata))
    # print(iterationsList)

    # iterations_fig, iterations_ax = plt.subplots()
    # iterations_ax.plot(range(len(iterationsList)), iterationsList)

    # iterations_ax.set_aspect("equal")
    # # plt.figure(figsize=(10,10))
    # plt.show()

    # print(selectionSortMetadata)
