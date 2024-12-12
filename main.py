import tkinter as tk
from tkinter import messagebox


def check_winner():
    """Check for a winning combination and handle the win scenario."""
    global winner
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            for i in combo:
                buttons[i].config(bg="yellow")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            winner = True
            disable_buttons()
            return
    
    
    
    # Check for a draw (if no empty buttons and no winner)
    if all(button["text"] != "" for button in buttons) and not winner:
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        disable_buttons()


def disable_buttons():
    """Disable all buttons after the game ends."""
    for button in buttons:
        button.config(state="disabled")


def button_click(index):
    """Handle button click events."""
    global current_player
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:
            toggle_player()


def toggle_player():
    """Switch the current player."""
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")


# Initialize main window
root = tk.Tk()
root.title("Tic-Tac-Toe")


# Initialize game state variables
current_player = "X"
winner = False


# Create a label to display the current player's turn
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)


# Create buttons for the Tic-Tac-Toe board
buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2,
                     command=lambda i=i: button_click(i)) for i in range(9)]


# Place buttons in a 3x3 grid
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)


# Run the Tkinter main loop
root.mainloop()
