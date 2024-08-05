rows = int(input())
cols = int(input())
paths = 0


def count_paths(rows, cols):
    if rows == 1 or cols == 1:
        return 1
    else:
        return count_paths(rows, cols - 1) + count_paths(rows - 1, cols)


print(count_paths(rows, cols))

# test inputs:

# 3
# 2

# 3
# 5
