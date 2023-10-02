import numpy as np
import math
import matplotlib.pyplot as plt


np.random.seed(1)


def SequencialSearch(key, arr):
    iterations = 0
    for i, ele in enumerate(arr):
        iterations += 1
        if (ele == key):
            return {"key": key, "index": i, "iterations": iterations}
    return {"index": -1, "iterations": iterations}


# Main execution
best_case = []
worst_case = []
avg_case = []

for i in range(1000, 5001, 1000):
    arr = list(range(1, i+1))
    np.random.shuffle(arr)
    # print(arr)

    # Searching the 1st element for best case
    best_case.append(SequencialSearch(arr[0], arr))

    # Searching the last element for worst case
    worst_case.append(SequencialSearch(arr[len(arr)-1], arr))

    random_index = math.ceil(np.random.rand() * i)
    # print(random_index)
    avg_case.append(SequencialSearch(arr[random_index], arr))

print(best_case)
print(worst_case)
print(avg_case)


# Generating the plots
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

X = range(1000, 5001, 1000)

ax1.plot(X, list(map(lambda data: data["iterations"], best_case)))
ax1.set(title="Best Case", xlabel="Inupt Length", ylabel="Iterations")

ax2.plot(X, list(map(lambda data: data["iterations"], avg_case)))
ax2.set(title="Average Case", xlabel="Inupt Length", ylabel="Iterations")

ax3.plot(X, list(map(lambda data: data["iterations"], worst_case)))
ax3.set(title="Worst Case", xlabel="Inupt Length", ylabel="Iterations")

fig.show()
