import tkinter as tk
from tkinter import messagebox

# Constants for the game
ROWS = 6
COLUMNS = 7
EMPTY = 0
YELLOW = 1
RED = 2

# Create the game window
window = tk.Tk()
window.title("Connect 4")

# Game board as a 2D array (6 rows, 7 columns)
board = [[EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]

# Track whose turn it is (1 for yellow, 2 for red)
current_player = YELLOW

# Button references for easy color change
buttons = []

def check_for_winner():
    """Checks the board for a winner (4 in a row, vertically, horizontally, or diagonally)."""
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if board[row][col] == current_player and all(board[row][col + i] == current_player for i in range(4)):
                return True

    # Check vertical
    for row in range(ROWS - 3):
        for col in range(COLUMNS):
            if board[row][col] == current_player and all(board[row + i][col] == current_player for i in range(4)):
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if board[row][col] == current_player and all(board[row + i][col + i] == current_player for i in range(4)):
                return True

    # Check diagonal (bottom-left to top-right)
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if board[row][col] == current_player and all(board[row - i][col + i] == current_player for i in range(4)):
                return True

    return False

def drop_piece(column):
    """Handles the logic for dropping a piece into the selected column."""
    global current_player

    # Find the lowest empty spot in the column
    for row in range(ROWS - 1, -1, -1):
        if board[row][column] == EMPTY:
            board[row][column] = current_player

            # Update the button color to represent the player's piece
            buttons[row][column].config(bg='yellow' if current_player == YELLOW else 'red')

            # Check if this move resulted in a win
            if check_for_winner():
                winner = "Yellow" if current_player == YELLOW else "Red"
                messagebox.showinfo("Game Over", f"{winner} wins!")
                reset_game()
            else:
                # Switch to the other player
                current_player = RED if current_player == YELLOW else YELLOW
            return

    # If the column is full
    messagebox.showwarning("Column Full", "This column is full! Choose another one.")

def create_board():
    """Creates the GUI board with clickable buttons."""
    for row in range(ROWS):
        button_row = []
        for col in range(COLUMNS):
            button = tk.Button(window, width=10, height=4, bg='white', command=lambda col=col: drop_piece(col))
            button.grid(row=row, column=col, padx=5, pady=5)
            button_row.append(button)
        buttons.append(button_row)

def reset_game():
    """Resets the game board to start a new game."""
    global board, current_player
    board = [[EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]
    current_player = YELLOW
    for row in buttons:
        for button in row:
            button.config(bg='white')

# Initialize the GUI board
create_board()

# Run the Tkinter event loop
window.mainloop()
