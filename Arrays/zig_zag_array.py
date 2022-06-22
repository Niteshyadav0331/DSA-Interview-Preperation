def zig_zag(arr, n):
    
    flag = True
    
    for i in range(n - 1):
        if flag is True:
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        else:
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        flag = bool(1 - flag)

    return arr

arr = [2, 6, 19, 26, 32]

print(arr)
zig_zag(arr, len(arr))

print(arr)
