def missing_no_in_an_array(arr):
    n = len(arr)

    sum1 = ((n + 1) * (n + 2) / 2)

    sum_of_arr = sum(arr)

    return sum1 - sum_of_arr

arr = [1, 2, 4, 5]

result = missing_no_in_an_array(arr)
print(result)