initial_list = list(map(int, input().split()))
number = int(input())


def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


print(binary_search(initial_list, number))

# test inputs:

# 1 2 3 4 5
# 1

# -1 0 1 2 4
# 1
