import matplotlib.pyplot as plt


def LinearSearch(key, arr):
    iterations = 0
    for i, ele in enumerate(arr):
        iterations += 1
        if (ele == key):
            return {"key": key, "index": i, "iterations": iterations}
    return {"index": -1, "iterations": iterations}


def BinarySearch(key, arr):
    iterations = 0
    start = 0
    end = len(arr)-1
    while (start <= end):
        iterations += 1
        mid = (start + end)//2
        if (arr[mid] < key):
            start = mid + 1
        elif (arr[mid] > key):
            end = mid - 1
        else:
            return {"key": key, "index": mid, "iterations": iterations}
    return {"key": key, "index": -1, "iterations": iterations}


# Main Execution
linear_search_data = []
binary_search_data = []

X = range(100, 501, 100)

for i in X:
    arr = list(range(1, i+1))

    # considering worst case time for both
    linear_search_data.append(LinearSearch(arr[len(arr)-1], arr))
    binary_search_data.append(BinarySearch(arr[len(arr)-1], arr))

print(linear_search_data)
print(binary_search_data)


# Generating the plots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))


ax1.plot(X, list(map(lambda data: data["iterations"], linear_search_data)))
ax1.set(title="Best Case", xlabel="Inupt Length", ylabel="Iterations")

ax2.plot(X, list(map(lambda data: data["iterations"], binary_search_data)))
ax2.set(title="Average Case", xlabel="Inupt Length", ylabel="Iterations")

plt.show()
