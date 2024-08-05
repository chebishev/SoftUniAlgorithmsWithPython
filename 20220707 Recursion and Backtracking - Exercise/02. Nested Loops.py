size = int(input())
output = size * [0]


def nest_loop(index, final_index, output_list):
    if index == final_index:
        print(" ".join([str(x) for x in output_list]))
        return
    for number in range(1, final_index + 1):
        output_list[index] = number
        nest_loop(index + 1, final_index, output_list)


nest_loop(0, size, output)

# test inputs:

# 2

# 3
