def merge_arrays(left, right):
    result = [None] * (len(left) + len(right))
    left_index = 0
    right_index = 0
    result_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result[result_index] = left[left_index]
            left_index += 1
        else:
            result[result_index] = right[right_index]
            right_index += 1
        result_index += 1

    while left_index < len(left):
        result[result_index] = left[left_index]
        left_index += 1
        result_index += 1

    while right_index < len(right):
        result[result_index] = right[right_index]
        right_index += 1
        result_index += 1

    return result


def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers

    mid = len(numbers) // 2
    left = numbers[:mid]
    right = numbers[mid:]

    return merge_arrays(merge_sort(left), merge_sort(right))


numbers = [int(x) for x in input().split()]
result = merge_sort(numbers)
print(*result, sep=" ")

# test inputs:
# 5 4 3 2 1

# 13 93 37 74 61 65 5 55 17 96 52 70 17 7 89 65 16 38 42 15 86 21 93 10 31 28 36 14 65 7 68 86 97 34 27 32 86 44 51 75 29 64 0 36 33 54 20 40 60 56 51 51 25 77 75 46 47 57 18 12 27 28 29 21 22 37 74 78 34 15 71 75 20 19 76 48 98 36 76 49 83 21 44 12 85 68 24 9 80 41 66 1 54 31 55 33 88 35 32 43
