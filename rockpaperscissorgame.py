
import tkinter as tk
import random

# Game logic
choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)
    result = get_winner(user_choice, computer_choice)

    # Update scores
    if "You win" in result:
        user_score += 1
    elif "Computer wins" in result:
        computer_score += 1

    # Update display
    user_choice_label.config(text=f"You chose: {user_choice}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score: You {user_score} - {computer_score} Computer")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="You chose:")
    computer_choice_label.config(text="Computer chose:")
    result_label.config(text="")
    score_label.config(text="Score: You 0 - 0 Computer")

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("350x400")
root.configure(bg="#f0f0f0")

title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

# Buttons
btn_rock = tk.Button(frame, text="Rock", width=10, command=lambda: play("rock"))
btn_paper = tk.Button(frame, text="Paper", width=10, command=lambda: play("paper"))
btn_scissors = tk.Button(frame, text="Scissors", width=10, command=lambda: play("scissors"))

btn_rock.grid(row=0, column=0, padx=5, pady=10)
btn_paper.grid(row=0, column=1, padx=5, pady=10)
btn_scissors.grid(row=0, column=2, padx=5, pady=10)

# Labels
user_choice_label = tk.Label(root, text="You chose:", font=("Arial", 12), bg="#f0f0f0")
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="Computer chose:", font=("Arial", 12), bg="#f0f0f0")
computer_choice_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score: You 0 - 0 Computer", font=("Arial", 12), bg="#f0f0f0")
score_label.pack()

# Reset Button
reset_btn = tk.Button(root, text="Reset Game", command=reset_game, bg="red", fg="white")
reset_btn.pack(pady=20)

# Start GUI
root.mainloop()
