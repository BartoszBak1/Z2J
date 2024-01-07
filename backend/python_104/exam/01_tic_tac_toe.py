import tkinter as tk
import random
import numpy as np


def computer_move():
    """This function randomly selects moves of the computer"""
    board = {
        1: btn_1,
        2: btn_2,
        3: btn_3,
        4: btn_4,
        5: btn_5,
        6: btn_6,
        7: btn_7,
        8: btn_8,
        9: btn_9,
    }

    # Check if there is empty field
    values = []
    for i in range(1, 10):
        values.append(board[i].cget("text"))
    if "" not in values:
        return False
    else:
        box_nr = random.randint(1, 9)
        print("Computer move: ", box_nr)
        while board[box_nr]["text"] != "":
            box_nr = random.randint(1, 9)
        btn = board[box_nr]
        btn["text"] = "O"


def check_win(matrix, n_rows, n_columns):
    """Function that checks the conditions of victory"""
    for i in range(n_rows):
        # print(i, ':', matrix[i])
        if matrix[i] == ["X"] * n_columns:
            msg = "Congratulations! You win! Restart game to play again"
            return msg
        if matrix[i] == ["O"] * n_columns:
            msg = "Sorry! You lose! Restart game to play again"
            return msg


def check_board():
    """Function that checks if somebody wins."""
    board = [
        [btn_1.cget("text"), btn_2.cget("text"), btn_3.cget("text")],
        [btn_4.cget("text"), btn_5.cget("text"), btn_6.cget("text")],
        [btn_7.cget("text"), btn_8.cget("text"), btn_9.cget("text")],
    ]
    # check rows

    msg = ""
    game_over = False

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

    if "" not in np.array(board) and msg is None:
        msg = "Is draw. Restart game to play again"

    if msg is None:
        msg = "Your move"
    else:
        game_over = True

    return game_over, msg


def click_box(btn):
    game_over, msg = check_board()
    lb["text"] = msg
    if game_over != True:
        if btn["text"] != "":
            lb["text"] = "This field is occupied. Please try another one."
        else:
            btn["text"] = "X"
            game_over, msg = check_board()
            lb["text"] = msg
            if game_over != True:
                computer_move()
                game_over, msg = check_board()
                lb["text"] = msg

    print(game_over)


def restart():
    board = {
        1: btn_1,
        2: btn_2,
        3: btn_3,
        4: btn_4,
        5: btn_5,
        6: btn_6,
        7: btn_7,
        8: btn_8,
        9: btn_9,
    }
    for button in board.values():
        button["text"] = ""


window = tk.Tk()
window.title("tic-tac-toe")
window.resizable(width=False, height=False)

frm_msg = tk.Frame(master=window)
frm_board = tk.Frame(master=window)
frm_btn = tk.Frame(master=window)

frm_msg.pack(padx=5, pady=5)
frm_board.pack(padx=5, pady=5)
frm_btn.pack(padx=5, pady=5)

frm_board.rowconfigure([0, 1, 2], minsize=100, weight=0)
frm_board.columnconfigure([0, 1, 2], minsize=100, weight=0)

# massage label
lb = tk.Label(master=frm_msg, text="Your move")
lb.pack()

btn_1 = tk.Button(master=frm_board, text="", command=lambda: click_box(btn_1))
btn_2 = tk.Button(master=frm_board, text="", command=lambda: click_box(btn_2))
btn_3 = tk.Button(master=frm_board, text="", command=lambda: click_box(btn_3))
btn_4 = tk.Button(master=frm_board, text="", command=lambda: click_box(btn_4))
btn_5 = tk.Button(master=frm_board, text="", command=lambda: click_box(btn_5))
btn_6 = tk.Button(master=frm_board, text="", command=lambda: click_box(btn_6))
btn_7 = tk.Button(master=frm_board, text="", command=lambda: click_box(btn_7))
btn_8 = tk.Button(master=frm_board, text="", command=lambda: click_box(btn_8))
btn_9 = tk.Button(master=frm_board, text="", command=lambda: click_box(btn_9))

# print board
buttons = [btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9]
n = 3
length = 9
i_coordinates = [i for i in range(n) for _ in range(n)]
j_coordinates = [i % n for i in range(length)]

for btn, i, j in zip(buttons, i_coordinates, j_coordinates):
    btn.grid(row=i, column=j, sticky="nsew")

# reset button
btn_reset = tk.Button(master=frm_btn, text="Reset", height=2, width=5, command=restart)
btn_reset.pack()

window.mainloop()
