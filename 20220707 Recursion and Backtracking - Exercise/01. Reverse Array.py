list_to_reverse = input().split()


def reverse_list(start_index, initial_list):
    if start_index == len(initial_list) // 2:
        return initial_list
    last_index = len(initial_list) - 1 - start_index
    initial_list[start_index], initial_list[last_index] = initial_list[last_index], initial_list[start_index]
    return reverse_list(start_index + 1, initial_list)


print(*reverse_list(0, list_to_reverse), sep=" ")

# test inputs:

# 1 2 3 4 5 6
