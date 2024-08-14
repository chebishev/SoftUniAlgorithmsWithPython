numbers = [int(x) for x in input().split()]


def quick_sort(start, end, numbers):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if numbers[left] > numbers[pivot] > numbers[right]:
            numbers[left], numbers[right] = numbers[right], numbers[left]
        if numbers[left] <= numbers[pivot]:
            left += 1
        if numbers[right] >= numbers[pivot]:
            right -= 1

    numbers[pivot], numbers[right] = numbers[right], numbers[pivot]
    quick_sort(start, right - 1, numbers)
    quick_sort(left, end, numbers)


quick_sort(0, len(numbers) - 1, numbers)
print(*numbers, sep=" ")

# test inputs:
# 5 4 3 2 1

# 13 93 37 74 61 65 5 55 17 96 52 70 17 7 89 65 16 38 42 15 86 21 93 10 31 28 36 14 65 7 68 86 97 34 27 32 86 44 51 75 29 64 0 36 33 54 20 40 60 56 51 51 25 77 75 46 47 57 18 12 27 28 29 21 22 37 74 78 34 15 71 75 20 19 76 48 98 36 76 49 83 21 44 12 85 68 24 9 80 41 66 1 54 31 55 33 88 35 32 43
