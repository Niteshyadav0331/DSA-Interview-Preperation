def reverse_in_groups(arr, n, k):
    i = 0
    while(i < n):
        left = i
        right = min(i + k - 1, n - 1)
        while (left < right):
            arr[left], arr[right] = arr[right], arr[left]

            left += 1
            right -= 1

        i += k

arr = [3, 7, 12, 15, 20, 25]
print(arr)
reverse_in_groups(arr, len(arr), 3)
print(arr)