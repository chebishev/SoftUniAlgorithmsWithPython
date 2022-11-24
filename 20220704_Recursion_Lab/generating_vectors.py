def vector_generating(number):
    for numbers in range(number):
        vector[index] = numbers
        vector_generating(ìndex + 1, vector)

number = int(input())

vector_generating()
