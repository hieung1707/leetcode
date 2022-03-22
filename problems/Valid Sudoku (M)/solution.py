def check_row(board: list, row):
    unique_values = []

    for column_index in range(9):
        if board[row][column_index] != "." and board[row][column_index] in unique_values:
            return False

        unique_values.append(board[row][column_index])

    return True


def check_column(board: list, column):
    unique_values = []

    for row_index in range(9):
        if board[row_index][column] != "." and board[row_index][column] in unique_values:
            return False

        unique_values.append(board[row_index][column])

    return True


def check_blocks(board: list):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            valid = check_block(board, i, j)

            if not valid:
                return False

    return True


def check_rows(board: list):
    for row_index in range(9):
        valid = check_row(board, row_index)

        if not valid:
            return False

    return True


def check_columns(board: list):
    for col_index in range(9):
        valid = check_column(board, col_index)

        if not valid:
            return False

    return True


def check_block(board: list, start_x: int, start_y: int):
    unique_values = []

    for row_index in range(start_x, start_x + 3):
        for col_index in range(start_y, start_y + 3):
            inspect_val = board[row_index][col_index]
            if inspect_val != "." and inspect_val in unique_values:
                return False

            unique_values.append(inspect_val)

    return True


def solution(board: list):
    return check_rows(board) and check_columns(board) and check_blocks(board)


def main():
    board = \
        [["8", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    print(solution(board))


if __name__ == "__main__":
    main()
