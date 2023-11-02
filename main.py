from tkinter import Tk, Button, messagebox

window = Tk()
window.title("Крестики-нолики")
window.geometry("280x300")

#    row   0    1    2       col
board = [[" ", " ", " "],  # 0
         [" ", " ", " "],  # 1
         [" ", " ", " "]]  # 2


def check_winner():
    # Проверка горизонталей
    if board[0][0] == board[0][1] == board[0][2] != " ":
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2] != " ":
        return board[1][0]
    if board[2][0] == board[2][1] == board[2][2] != " ":
        return board[2][0]

    # Проверка вертикалей
    if board[0][0] == board[1][0] == board[2][0] != " ":
        return board[0][0]
    if board[0][1] == board[1][1] == board[2][1] != " ":
        return board[0][1]
    if board[0][2] == board[1][2] == board[2][2] != " ":
        return board[0][2]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return False


def make_move(button, row, col):
    global current_player
    if board[row][col] == " ":
        board[row][col] = current_player
        button["text"] = current_player
        winner = check_winner()
        if winner:
            messagebox.showinfo("Конец игры!", f"Игрок {winner} победил!")
            window.quit()
        elif all(board[i][j] != " " for i in range(3) for j in range(3)):
            messagebox.showinfo("Конец игры", "Ничья...")
            window.quit()
        if current_player == "X":
            current_player = "0"
        else:
            current_player = "X"


current_player = "X"

button_font = ("Arial", 20)

for i in range(3):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

default_font = ("Arial", 20)
button_style = {"font": default_font, "width": 5, "height": 2}

b0 = Button(text=" ", command=lambda row=0, col=0: make_move(b0, row, col), **button_style)
b0.grid(row=0, column=0, sticky="nsew")

b1 = Button(text=" ", command=lambda row=0, col=1: make_move(b1, row, col), **button_style)
b1.grid(row=0, column=1, sticky="nsew")

b2 = Button(text=" ", command=lambda row=0, col=2: make_move(b2, row, col), **button_style)
b2.grid(row=0, column=2, sticky="nsew")

b3 = Button(text=" ", command=lambda row=1, col=0: make_move(b3, row, col), **button_style)
b3.grid(row=1, column=0, sticky="nsew")

b4 = Button(text=" ", command=lambda row=1, col=1: make_move(b4, row, col), **button_style)
b4.grid(row=1, column=1, sticky="nsew")

b5 = Button(text=" ", command=lambda row=1, col=2: make_move(b5, row, col), **button_style)
b5.grid(row=1, column=2, sticky="nsew")

b6 = Button(text=" ", command=lambda row=2, col=0: make_move(b6, row, col), **button_style)
b6.grid(row=2, column=0, sticky="nsew")

b7 = Button(text=" ", command=lambda row=2, col=1: make_move(b7, row, col), **button_style)
b7.grid(row=2, column=1, sticky="nsew")

b8 = Button(text=" ", command=lambda row=2, col=2: make_move(b8, row, col), **button_style)
b8.grid(row=2, column=2, sticky="nsew")

window.mainloop()
