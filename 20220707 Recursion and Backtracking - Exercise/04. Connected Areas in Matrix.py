rows = int(input())
cols = int(input())
matrix = []
areas = []

for _ in range(rows):
    matrix.append(list(input()))


def find_areas(row, col, matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0
    if matrix[row][col] != "-":
        return 0

    matrix[row][col] = "v"

    result = 1
    result += find_areas(row - 1, col, matrix)
    result += find_areas(row + 1, col, matrix)
    result += find_areas(row, col - 1, matrix)
    result += find_areas(row, col + 1, matrix)

    return result


for row in range(rows):
    for col in range(cols):
        size = find_areas(row, col, matrix)
        if size == 0:
            continue

        areas.append((size, row, col))

print("Total areas found:", len(areas))
for index,area in enumerate(sorted(areas, key=lambda x: x[0], reverse=True)):
    print(f"Area #{index + 1} at ({area[1]}, {area[2]}), size: {area[0]}")

# test inputs:

# 4
# 9
# ---*---*-
# ---*---*-
# ---*---*-
# ----*-*--

# 5
# 10
# *--*---*--
# *--*---*--
# *--*****--
# *--*---*--
# *--*---*--
