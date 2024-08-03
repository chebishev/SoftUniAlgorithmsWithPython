board_size = 8
board = []

for _ in range(board_size):
    board.append(["-"] * board_size)


def draw_queens(row, board, rows, cols, left, right):

    if row == board_size:
        for row in board:
            print(" ".join(row))
        print()
        return

    for col in range(board_size):
        if row in rows:
            continue
        if col in cols:
            continue
        left_diagonals = row - col
        if left_diagonals in left:
            continue
        right_diagonals = row + col
        if right_diagonals in right:
            continue

        board[row][col] = "*"
        rows.add(row)
        cols.add(col)
        left.add(left_diagonals)
        right.add(right_diagonals)
        draw_queens(row + 1, board, rows, cols, left, right)
        board[row][col] = "-"
        rows.remove(row)
        cols.remove(col)
        left.remove(left_diagonals)
        right.remove(right_diagonals)
        board[row][col] = "-"


draw_queens(0, board, set(), set(), set(), set())
