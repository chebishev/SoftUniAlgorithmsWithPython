def calc_sum(numbers, index):
    if index == len(numbers) - 1:
        return numbers[index]
    return numbers[index] + calc_sum(numbers, index + 1)


numbers = [int(number) for number in input().split()]

print(calc_sum(numbers, 0))
# test input 1 2 3 4
# test input -1 0 1
