def equilibrium_point(arr, n):
    total_sum, sum = 0, 0

    for i in range(n):
        total_sum += arr[i]

    for i in range(n):
        if (sum == (total_sum - sum - arr[i])):
            return i + 1

        sum += arr[i]

    return -1

arr = [2, 3, 4, 6, 2, 2, 2, 2, 1]
n = len(arr)

result = equilibrium_point(arr, n)

print(result)