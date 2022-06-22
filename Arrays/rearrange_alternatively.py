def rearrange_alternatively(arr, n):
    temp = n * [None]
    flag = True

    low = 0
    high = n - 1
    for i in range(n):
        if flag is True:
            temp[i] = arr[high]
            high -= 1

        else:
            temp[i] = arr[low]
            low += 1

        flag = bool(1 - flag)

    for i in range(n):
        arr[i] = temp[i]

    return arr

arr = [2, 6, 19, 26, 32]

print(arr)
rearrange_alternatively(arr, len(arr))

print(arr)
