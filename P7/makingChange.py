def make_a_change(d, N):
    n = len(d)
    C = [[0 if j == 0 else float('inf') for j in range(N + 1)]
         for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, N + 1):
            if i == 1 and j < d[i - 1]:
                C[i][j] = float('inf')
            elif i == 1:
                C[i][j] = 1 + C[1][j - d[i - 1]]
            elif j < d[i - 1]:
                C[i][j] = C[i - 1][j]
            else:
                C[i][j] = min(C[i - 1][j], 1 + C[i][j - d[i - 1]])

    return C[n][N]


# testing
x = make_a_change([1, 5, 10, 25], 130)

print(x)
