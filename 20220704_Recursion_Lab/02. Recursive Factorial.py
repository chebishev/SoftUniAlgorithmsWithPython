def calculate_factorial(number):
    return 1 if number == 0 else number * calculate_factorial(number - 1)


print(calculate_factorial(int(input())))

# test inputs:

# 5

# 10
