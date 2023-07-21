#!/usr/bin/python3
"""The numbers guessing game
The program chooses a random number and the user tries to guess
the number. The program gives feedback on whether it's too high,
too low, or the correct guess.
"""
import random

EASY_LEVEL = 10
HARD_LEVEL = 5


def set_difficulty(choice):
    """
    Sets the difficulty of the game as `easy` or `hard` based on
    user preference

    Args:
        choice (str): user preference of difficulty
    Return:
        number of attempts based on choice
    """
    if choice == 'easy':
        return EASY_LEVEL
    elif choice == 'hard':
        return HARD_LEVEL
    else:
        return HARD_LEVEL


def compare_answer(guess, answer, turns):
    """
    Checks the guess against the answer, and returns
    the number of turns remaining

    Args:
        answer (int): a random number generated by the program
        guess (int): user prediction of the answer
        turns (int): number of attempts to make a guess
    """
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1


def play(attempts):
    """Driver code for the guessing game

    Args:
        attempts (int): number of attempts to make a guess
        number (int): random number generated by program
    """
    guess = None
    while guess != number:
        print("You have {} attempts".format(attempts))
        guess = int(input(("\nMake a guess:\n")))
        attempts = compare_answer(guess, number, attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose")
            return
    print("You got it! {}".format(number))


# ###################### THE GAME ##########################
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Pick a random number for the user to guess
number = random.randint(1, 100)

# Ask user to choose their level
difficulty = input("Choose a difficulty: 'easy' or 'hard'\n")

# Set number of attempts depending on level picked
attempts = set_difficulty(difficulty)

# call the function to play the game
play(attempts)