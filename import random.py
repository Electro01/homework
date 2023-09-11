import random
import math
import tkinter as tk
from tkinter import simpledialog, messagebox

# Initialize global variables
secret_number = 0
num_range = 100
num_guesses = 7

# Function to start a new game
def new_game():
    global secret_number, num_range, num_guesses
    secret_number = random.randint(0, num_range - 1)
    num_guesses = int(math.ceil(math.log2(num_range)))
    messagebox.showinfo("New Game", f"New game. Range is from 0 to {num_range}. Number of remaining guesses is {num_guesses}.")
    take_guess()

# Function to handle player's guess
def take_guess():
    global num_guesses
    guess = simpledialog.askinteger("Guess the Number", "Enter your guess:")
    
    if guess is None:
        return

    num_guesses -= 1

    if guess < secret_number:
        messagebox.showinfo("Result", f"Higher! Number of remaining guesses is {num_guesses}.")
        if num_guesses > 0:
            take_guess()
        else:
            messagebox.showinfo("Game Over", f"Out of guesses! The secret number was {secret_number}.")
            new_game()
    elif guess > secret_number:
        messagebox.showinfo("Result", f"Lower! Number of remaining guesses is {num_guesses}.")
        if num_guesses > 0:
            take_guess()
        else:
            messagebox.showinfo("Game Over", f"Out of guesses! The secret number was {secret_number}.")
            new_game()
    else:
        messagebox.showinfo("Result", f"Correct! The secret number was {secret_number}.")
        new_game()

# Function to start a game with the range [0, 100)
def range100():
    global num_range
    num_range = 100
    new_game()

# Function to start a game with the range [0, 1000)
def range1000():
    global num_range
    num_range = 1000
    new_game()

# Create a Tkinter window
window = tk.Tk()
window.title("Guess the Number")

# Add buttons
btn_range100 = tk.Button(window, text="Range is [0, 100)", command=range100)
btn_range1000 = tk.Button(window, text="Range is [0, 1000)", command=range1000)

btn_range100.pack()
btn_range1000.pack()

# Start the game initially
new_game()

# Start the Tkinter main loop
window.mainloop()
