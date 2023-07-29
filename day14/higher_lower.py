#!/usr/bin/python3

"""
Higher/Lower game: compares two random values from the game data
based on their follower counts
"""
# import the random module
import random
# import the list of dictionaries containing 'players' and art logos
from game_data import data
from art import logo, vs


def pick_person():
    """Picks a random person dict from the game data

    Return:
        a random person's dictionary from the list
    """
    player = random.choice(data)
    return player


def format_person(player):
    """Formats the content of person dict into readable format

    Args:
        player (dict): data containing player information
    Returns:
        formatted string representation of player
    """
    name = player["name"]
    career = player["description"]
    country = player["country"]
    followers = player["follower_count"]
    return "{}, a {} from {}".format(name, career, country)


def pick_again(winner):
    """Generates a new random player for the next round
    to play against the winner

    Args:
        winner (dict): dict item of winning player
    """
    new_a = winner
    new_b = pick_person()
    while new_a == new_b:
        new_b = pick_person()
    compare(new_a, new_b)


def compare(a, b):
    """Compares the follower count of player a and player b
    against user guess

    Args:
        a (dict): dictionary of random player a information
        b (dict): dictionary of random player b information
    """
    global score

    print("Compare A: {}".format(format_person(a)))
    print(vs)
    print("Against B: {}".format(format_person(b)))

    answer = input("Who has more followers?: ").lower()
    a_count = a["follower_count"]
    b_count = b["follower_count"]

    # Cases: a is answer and a > b || b is answer and b > a
    if answer == 'a' and a_count > b_count:
        score += 1
        print("You're right. Current score: {}\n".format(score))
        pick_again(a)
    elif answer == 'b' and a_count < b_count:
        score += 1
        print("You're right. Current score: {}\n".format(score))
        pick_again(b)
    else:
        print("That's wrong\n")
        print("Final Score: {}".format(score))


score = 0
print(logo)
a = pick_person()
b = pick_person()
while a == b:
    b = pick_person()


compare(a, b)
