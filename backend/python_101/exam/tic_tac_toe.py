import random
import numpy as np


def print_board(board):
    """Function that prints what the board looks like."""
    print(
        f"""Board:
    {board[0]}
    {board[1]}
    {board[2]}"""
    )


def check_win(matrix, n_rows, n_columns):
    """Function that checks the conditions of victory"""
    for i in range(n_rows):
        # print(i, ':', matrix[i])
        if matrix[i] == ["X"] * n_columns:
            msg = "Congratulations! You win!"
            return msg
        if matrix[i] == ["O"] * n_columns:
            msg = "Sorry! You lose!"
            return msg


def check_board(board):
    """Function that checks if somebody wins."""
    # check rows
    msg = ""
    if msg == "":
        msg = check_win(board, 3, 3)
    # check columns
    if msg is None:
        board_transpose = np.array(board).T.tolist()
        msg = check_win(board_transpose, 3, 3)
    # check diagonals
    if msg is None:
        diagonal = np.diagonal(np.array(board)).tolist()
        second_diagonal = np.diagonal(np.fliplr(np.array(board))).tolist()
        diagonals = [diagonal, second_diagonal]
        msg = check_win(diagonals, 2, 3)
    return msg


def get_coordinate_from_computer():
    """This function randomly selects moves of the computer"""
    row = random.randint(0, 2)
    column = random.randint(0, 2)

    return row, column


def get_coordinate_from_user(axis):
    """This function gets the user's moves"""
    while True:
        try:
            coordinate = int(input(f"Enter number of {axis}: ")) - 1
            if coordinate in range(0, 3):
                break
            else:
                print(f"The {axis} coordinate should be within the range from 1 to 3")
        except ValueError:
            print("The row and column coordinates should be integer.")

    return coordinate


counter = 0  # This variable is used to count user moves.
board = [["", "", ""], ["", "", ""], ["", "", ""]]  # Set plain board.

print(
    """Hello this is the tic tac toe game.
         You are X and computer is O.
         You insert X by choice number of row and number of column on board 3X3.
         You can chose numbers from 1 to 3.
      """
)
# main program
while True:
    print_board(board)
    #  user move
    usr_row, usr_column = get_coordinate_from_user(
        axis="row"
    ), get_coordinate_from_user(axis="column")
    # Check if selected field is occupied.
    while board[usr_row][usr_column] != "":
        print("This field is occupied. Please choose another one.")
        usr_row, usr_column = get_coordinate_from_user(
            axis="row"
        ), get_coordinate_from_user(axis="column")
    # save user move
    board[usr_row][usr_column] = "X"

    counter = counter + 1
    if counter < 5:  # If the user makes 5 moves, the game should end.
        # computer move
        com_row, com_column = get_coordinate_from_computer()
        # Check if selected field is occupied.
        while board[com_row][com_column] != "":
            com_row, com_column = get_coordinate_from_computer()
        # save computer move
        board[com_row][com_column] = "O"

    msg = check_board(board)
    # Check if somebody wins.
    # print_board(board)
    if msg is not None:
        print(msg)
        print_board(board)
        response = " "
        while "ny".find(response) == -1:
            response = input("Do you want to play again? y/n: ").lower()
        if response == "y":
            board = [["", "", ""], ["", "", ""], ["", "", ""]]
            counter = 0
        elif response == "n":
            print("Thanks. Goodbye!")
            break
    if msg is None and counter == 5:  # what if is draw
        print("Is draw!")
        print_board(board)
        response = " "
        while "ny".find(response) == -1:
            response = input("Do you want to play again? y/n: ").lower()
            print(response)
        if response == "y":
            board = [["", "", ""], ["", "", ""], ["", "", ""]]
            counter = 0
            continue
        elif response == "n":
            print("The End")
            break
