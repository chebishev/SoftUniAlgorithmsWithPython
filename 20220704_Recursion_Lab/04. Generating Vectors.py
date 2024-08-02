def generate_01_vectors(index, vector):
    if index == len(vector):
        print("".join([str(number) for number in vector]))
        return

    for number in range(2):
        vector[index] = number
        generate_01_vectors(index + 1, vector)


vector = int(input()) * [0]
generate_01_vectors(0, vector)

# test inputs:

# 3

# 5
