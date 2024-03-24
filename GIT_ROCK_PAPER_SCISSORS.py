import random

def get_user_choice():
    while True:
        user_input = input("Type rock/paper/scissors or Q to quit: ").lower()
        if user_input == "q":
            return None
        elif user_input in options:
            return user_input
        else:
            print("Invalid input. Please type rock, paper, scissors, or Q to quit.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You won! :)"
    else:
        return "You lost! *sad*"

def print_score(user_wins, computer_wins):
    print("You won", user_wins, "times.")
    print("The computer won", computer_wins, "times.")
    print("Peace x_x")

options = ["rock", "paper", "scissors"]
user_wins = 0
computer_wins = 0

while True:
    user_choice = get_user_choice()
    if user_choice is None:
        break

    computer_choice = random.choice(options)
    print("The computer has picked", computer_choice + ".")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    if "won" in result:
        user_wins += 1
    elif "lost" in result:
        computer_wins += 1

print_score(user_wins, computer_wins)
