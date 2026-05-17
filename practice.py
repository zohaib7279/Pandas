from tkinter import *
from tkinter import messagebox

# ---------------- WINDOW ---------------- #

root = Tk()
root.title("Tic Tac Toe")
root.geometry("350x450")
root.config(bg="#1e1e1e")

# ---------------- VARIABLES ---------------- #

current_player = "X"

board = ["", "", "", "", "", "", "", "", ""]

buttons = []

# ---------------- STATUS LABEL ---------------- #

status = Label(
    root,
    text="Player X Turn",
    font=("Arial", 20, "bold"),
    bg="#1e1e1e",
    fg="white"
)

status.pack(pady=20)

# ---------------- GAME FRAME ---------------- #

frame = Frame(root, bg="#1e1e1e")

frame.pack()

# ---------------- WINNING CONDITIONS ---------------- #

winning_conditions = [

    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],

    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],

    [0, 4, 8],
    [2, 4, 6]

]

# ---------------- CHECK WINNER ---------------- #

def check_winner():

    global current_player

    for condition in winning_conditions:

        a, b, c = condition

        if board[a] == board[b] == board[c] != "":

            status.config(
                text=f"Player {board[a]} Wins!"
            )

            messagebox.showinfo(
                "Winner",
                f"Player {board[a]} Wins!"
            )

            disable_buttons()

            return

    if "" not in board:

        status.config(text="Game Draw!")

        messagebox.showinfo(
            "Draw",
            "Game Draw!"
        )

        return

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    status.config(
        text=f"Player {current_player} Turn"
    )

# ---------------- BUTTON CLICK ---------------- #

def button_click(index):

    global current_player

    if board[index] == "":

        board[index] = current_player

        buttons[index].config(
            text=current_player
        )

        check_winner()

# ---------------- DISABLE BUTTONS ---------------- #

def disable_buttons():

    for button in buttons:

        button.config(
            state=DISABLED
        )

# ---------------- RESTART GAME ---------------- #

def restart_game():

    global current_player
    global board

    current_player = "X"

    board = ["", "", "", "", "", "", "", "", ""]

    status.config(
        text="Player X Turn"
    )

    for button in buttons:

        button.config(
            text="",
            state=NORMAL
        )

# ---------------- CREATE BUTTONS ---------------- #

for i in range(9):

    button = Button(

        frame,

        text="",

        font=("Arial", 25, "bold"),

        width=5,
        height=2,

        bg="white",

        command=lambda i=i: button_click(i)

    )

    button.grid(

        row=i // 3,
        column=i % 3,

        padx=5,
        pady=5

    )

    buttons.append(button)

# ---------------- RESTART BUTTON ---------------- #

restart_btn = Button(

    root,

    text="Restart Game",

    font=("Arial", 14, "bold"),

    bg="#333",

    fg="white",

    command=restart_game

)

restart_btn.pack(pady=20)

# ---------------- RUN WINDOW ---------------- #

root.mainloop()