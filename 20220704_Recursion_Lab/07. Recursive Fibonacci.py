number = int(input())
fibonacci_0 = 1
fibonacci_1 = 1

for _ in range(number - 1):
    fibonacci_0, fibonacci_1 = fibonacci_1, fibonacci_0 + fibonacci_1

print(fibonacci_1)