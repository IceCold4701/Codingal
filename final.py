import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice):
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    
    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    result_label.config(text=f"You chose {user_choice}\nComputer chose {computer_choice}\n{result}")

# Set up the window
root = tk.Tk()
root.geometry("400x400")
root.title("Length Converter App")  # As you requested, using this title even though it's RPS game

# Instructions
label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14))
label.pack(pady=20)

# Buttons for user choice
button_frame = tk.Frame(root)
button_frame.pack()

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: determine_winner("rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: determine_winner("paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: determine_winner("scissors"))
scissors_button.grid(row=0, column=2, padx=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=30)

# Start the GUI loop
root.mainloop()
