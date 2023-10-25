def fractional_knapsack(weights, values, knapsack_capacity):
    n = len(weights)
    # calculating the value per weight ratio
    value_per_weight = [
        (values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    value_per_weight.sort(reverse=True, key=lambda x: x[0])

    total_value = 0
    selected_items = []
    remaining_capacity = knapsack_capacity

    for ratio, weight, value in value_per_weight:
        if remaining_capacity >= weight:
            # Take whole object
            total_value += value
            selected_items.append((weight, value))
            remaining_capacity -= weight
        else:
            # take fraction of the remaining object and exit
            fraction = remaining_capacity / weight
            total_value += fraction * value
            selected_items.append((remaining_capacity, fraction * value))
            break  # Knapsack is full

        # check if capacity is full
        if not remaining_capacity:
            break

    return total_value, selected_items


# Example usage
weights = [5, 7, 3, 2, 6]
values = [30, 15, 25, 12, 20]
knapsack_capacity = 10

total_value, selected_items = fractional_knapsack(
    weights, values, knapsack_capacity)

print("Total Value:", total_value)
# output in form of array of (corresponding weight(fraction),value)
print("Selected Items:", selected_items)
