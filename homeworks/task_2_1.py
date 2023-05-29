def minimum(arr):
    min_number = arr[0]
    for num in arr:
        if num < min_number:
            min_number = num

    return min_number


def maximum(arr):
    max_number = arr[0]
    for num in arr:
        if num > max_number:
            max_number = num

    return max_number