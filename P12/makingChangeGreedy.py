def making_change(amount, denominations):
    denominations.sort(reverse=True)
    coin_counts = [[i, 0] for i in denominations]
    for i, coin in enumerate(denominations):
        while amount >= coin:
            amount -= coin
            coin_counts[i][1] += 1

    return coin_counts


# Example usage
amount = 42
denominations = [1, 5, 10, 25]
coin_counts = making_change(amount, denominations)
# in format [denomination, count]
print(f"For {amount},change is:", coin_counts)
