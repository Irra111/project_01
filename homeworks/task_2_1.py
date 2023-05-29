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

assert maximum([4,6,2,1,9,63,-134,566]) == 566
assert minimum([4,6,2,1,9,63,-134,566]) == -134
assert maximum([-52, 56, 30, 29, -54, 0, -110]) == 56
assert minimum([-52, 56, 30, 29, -54, 0, -110]) == -110
assert maximum([42, 54, 65, 87, 0]) == 87
assert minimum([42, 54, 65, 87, 0]) == 0
assert maximum([5]) == 5
assert minimum([5]) == 5