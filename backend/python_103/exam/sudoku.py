import random


def generate_small_board():
    small_board = []
    while len(small_board) < 9:
        number = random.randint(1, 9)
        if number not in small_board:
            small_board.append(number)
    return [small_board[i : i + 3] for i in range(0, len(small_board), 3)]


def generate_big_board():
    disordered_big_board = []
    big_board = []
    for i in range(9):
        disordered_big_board.append(generate_small_board())

    for i in range(0, 9, 3):
        board_third = disordered_big_board[i : i + 3]
        for j in range(0, 3):
            nested_row_of_big_board = []
            for k in range(0, 3):
                nested_row_of_big_board.append(board_third[k][j])
            row_of_big_board = [
                item for sublist in nested_row_of_big_board for item in sublist
            ]
            big_board.append(row_of_big_board)

    return big_board


def print_board(board):
    for row in board:
        print(row)


def check(list):
    if len(set(list)) == len(list):
        return True
    else:
        return False


def check_rows(board):
    for row in board:
        response = check(row)
        if response:
            continue
        else:
            return response
    return True

def check_columns(board):
    for i in range(9):
        # transpose column to list
        column = []
        for row in board:
            column.append(row[i])
        # check column
        response = check(column)
        if response:
            continue
        else:
            return response
    return True

def check_board(board):
    row_status = check_rows(board)
    columns_status = check_columns(board)

    return {"row status": row_status, "column status": columns_status}


# Check
board = generate_big_board()
print_board(board)
print(check_board(board))

# Check correct board
correct_board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]
print("Check correct board:")
print_board(board)
print(check_board(correct_board))

board = [
    [9, 2, 3, 6, 2, 4, 5, 1, 4],
    [1, 7, 8, 3, 9, 7, 6, 7, 2],
    [4, 5, 6, 1, 8, 5, 8, 3, 9],
    [3, 1, 4, 5, 4, 2, 7, 8, 5],
    [7, 5, 6, 7, 9, 8, 6, 9, 4],
    [9, 8, 2, 3, 1, 6, 1, 3, 2],
    [2, 3, 1, 1, 6, 7, 5, 8, 2],
    [7, 5, 9, 4, 8, 9, 3, 4, 9],
    [6, 8, 4, 3, 5, 2, 7, 1, 6],
]
