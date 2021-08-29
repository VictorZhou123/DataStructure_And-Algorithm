li = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50],
]

def select(num, li, m, n):
    for i in range(m):
        if li[i][n-1] >= num:
            for j in range(n):
                if li[i][j] == num:
                    return True
    return False

def binary_search(target, matrix, m, n):
    left = 0
    right = m * n -1
    while left <= right:
        mid = (left + right) // 2
        i = mid // n
        j = mid % n
        if matrix[i][j] == target:
            return True
        if matrix[i][j] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False


res = binary_search(31, li, 3, 4)
print(res)