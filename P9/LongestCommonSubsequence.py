def lcs_length_table(X, Y):
    m = len(X)
    n = len(Y)

    # constructing the empty tables of n x m size
    C = [[0] * (n + 1) for _ in range(m + 1)]
    B = [[''] * (n + 1) for _ in range(m + 1)]

    # Filling values in tabels
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
                B[i][j] = 'D'  # 'D' for diagonal, this value tell the inherited value
            else:
                if C[i - 1][j] >= C[i][j - 1]:
                    C[i][j] = C[i - 1][j]
                    B[i][j] = 'U'  # 'U' for up
                else:
                    C[i][j] = C[i][j - 1]
                    B[i][j] = 'L'  # 'L' for left

    return C, B


def print_lcs(B, X, i, j):

    # backtracking to generate sequence
    if i == 0 or j == 0:
        return ""
    if B[i][j] == 'D':
        return print_lcs(B, X, i - 1, j - 1) + X[i - 1]
    elif B[i][j] == 'U':
        return print_lcs(B, X, i - 1, j)
    else:
        return print_lcs(B, X, i, j - 1)


# Example usage
X = "PANCHAL"
Y = "DHYANESH"
C, B = lcs_length_table(X, Y)
lcs = print_lcs(B, X, len(X), len(Y))
print("Length of Longest Common Subsequence:", C[len(Y)-1][len(X)+1])
print("Longest Common Subsequence:", lcs)
