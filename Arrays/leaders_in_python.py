def leaders(arr, n):
    A = []
    
    max_from_right = float('-inf')

    for i in range(n - 1, -1, -1):
        if (arr[i] >= max_from_right):
            A.append(arr[i])
            max_from_right = arr[i]

    return A[::-1]

arr = [18, 20, 7, 2, 5, 1]
n = len(arr)

result = leaders(arr, n)

print(result)