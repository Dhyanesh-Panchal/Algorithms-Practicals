def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        m[i][i] = 0

    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return (m, s)


# Example matrix chain dimensions
matrix_dimensions = [30, 35, 15, 5, 10, 20, 25]  # it represents 30x35*35x15...
(m, s) = matrix_chain_order(matrix_dimensions)

# Print the matrices m and s
print("Matrix m:")
for row in m:
    print(row)

print("\nMatrix s:")
for row in s:
    print(row)
