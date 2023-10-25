def binary_knapsack(w, v, M):
    n = len(w)
    V = [[0 for _ in range(M + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(M + 1):
            if w[i - 1] <= j:
                V[i][j] = max(V[i - 1][j], v[i - 1] + V[i - 1][j - w[i - 1]])
            else:
                V[i][j] = V[i - 1][j]

    return V


def trace_knapsack(w, v, V, M):
    n = len(w)
    selected_items = []
    total_value = V[n][M]
    i, j = n, M

    while i > 0 and j > 0:
        if V[i][j] != V[i - 1][j]:
            selected_items.append(i - 1)  # Adjust for 0-based index
            j -= w[i - 1]
        i -= 1

    selected_items.reverse()
    return selected_items, total_value


weights = [1, 2, 5, 6, 7]
values = [1, 6, 18, 22, 28]
knapsack_capacity = 11

# Solve knapsack problem and generate table
V = binary_knapsack(weights, values, knapsack_capacity)

# Trace the table to get selected items indx and total value
selected_items_indx, total_value = trace_knapsack(
    weights, values, V, knapsack_capacity)

print("The Selected Items indices are:", selected_items_indx)
print("Total Value:", total_value)
