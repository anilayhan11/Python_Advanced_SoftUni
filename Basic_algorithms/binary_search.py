A = [-3, -1, 0, 1, 4, 7]


# Traditional Binary Search - Looking up if number is in array:
# Time: O(log n)
# Space: O(1)

def binary_search(arr, target):
    N = len(arr)
    L = 0
    R = N - 1

    while L <= R:
        M = L + ((R - L) // 2)

        if arr[M] == target:
            return True
        elif target < arr[M]:
            R = M - 1
        else:
            L = M + 1

    return False


print(binary_search(A, -2))
