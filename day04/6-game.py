# ROCK, PAPER, SCISSORS

import random
print("Welcome to the Rock, Paper, Scissors game")
# zero = "Rock"
# one = "Paper"
# two = "Scissors"

choice = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors:\n"))

# game logic
opponent = random.randint(0, 2)
print(f"Computer chose {opponent}")
if choice > 2 or choice < 0:
    print("Invalid choice. You lose!")
elif choice == opponent:
    print("It's a draw")
elif choice < opponent:
    print("You lose!")
elif choice > opponent:
    print("You win!")
