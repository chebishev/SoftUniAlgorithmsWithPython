rows = int(input())
cols = int(input())

labyrinth = []
for _ in range(rows):
    row = list(input())
    labyrinth.append(row)


def find_paths(row, col, direction, matrix, path):
    if col < 0 or col >= len(matrix[0]) or row < 0 or row >= len(matrix):
        return
    if matrix[row][col] == "v":
        return
    if matrix[row][col] == "*":
        return

    path.append(direction)

    if matrix[row][col] == "e":
        print("".join(path))
    else:
        matrix[row][col] = "v"
        find_paths(row, col + 1, "R", matrix, path)
        find_paths(row + 1, col, "D", matrix, path)
        find_paths(row, col - 1, "L", matrix, path)
        find_paths(row - 1, col, "U", matrix, path)
        matrix[row][col] = "-"

    path.pop()


find_paths(0, 0, "", labyrinth, [])

# test inputs:

# 3
# 3
# ---
# -*-
# --e

# 3
# 5
# -**-e
# -----
# *****
