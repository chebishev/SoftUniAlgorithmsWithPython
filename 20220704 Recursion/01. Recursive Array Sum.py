def sum_list(numbers, index):
    if index == len(numbers) - 1:
        return numbers[index]
    return numbers[index] + sum_list(numbers, index + 1)


numbers_list = [int(number) for number in input().split()]
print(sum_list(numbers_list, 0))

# test inputs:

# 1 2 3 4

# -1 0 1
