# 3 size of matrix
# 11 2 4
# 4 5 6
# 10 8 -12


def diagonalDifference(arr):
    principal = 0
    secondary = 0
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n):

            # Condition for principal diagonal
            if (i == j):
                principal += arr[i][j]

            # Condition for secondary diagonal
            if ((i + j) == (n - 1)):
                secondary += arr[i][j]
    return secondary - principal

# n = int(input().strip())
n = 3
arr = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

# for _ in range(n):
#     arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print(result)
