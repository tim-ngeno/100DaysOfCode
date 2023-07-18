"""Blackjack Game - Capstone project"""

import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Deals a random card from the deck of cards"""
    return random.choice(cards)


def print_cards():
    """Displays the cards that have been dealt"""
    print("Your cards: {}, current score: {}".format(
        user_cards, user_score))
    print("Computer's cards: [{}]".format(comp_cards[0]))


def calculate_score(cards_list):
    """
    Returns the total score from cards input
    The score checks for a blackjack(A hand with only 2 hands: ace +
    10), and returns 0 instead of the actual score.

     Args:
        cards_list (list): a list containing dealt cards
    """
    # Check for a Blackjack
    if sum(cards_list) == 21 and len(cards_list) == 2:
        return 0
    if sum(cards_list) > 21 and 11 in cards_list:
        cards_list.remove(11)
        cards_list.append(1)
    return sum(cards_list)


def compare(user, dealer):
    """
    Compares the scores to determine the winner
    Args:
        user (int): the user score
        dealer (int): the dealer score
    """
    if user == dealer:
        return "It's a draw! 😒"
    elif dealer == 0:
        return "You lose, opponent has a Blackjack 🤡"
    elif user == 0:
        return "You Win!! BLACKJACK!!! 🥳"
    elif user > 21:
        return "You went over 21, loser!"
    elif dealer > 21:
        return "Opponent went over 21. You win lucky duck"
    elif user > dealer:
        return "User wins! 😜"
    elif dealer > user:
        return "Dealer wins! 🤨"


# deal both user and computer two random starting cards
user_cards = []
comp_cards = []
for _ in range(2):
    user_cards.append(deal_card())
    comp_cards.append(deal_card())


print("Let's play some Blackjack!!\n")

game_over = False
while not game_over:
    print(logo)
    # Calculate the scores
    user_score = calculate_score(user_cards)
    comp_score = calculate_score(comp_cards)
    print_cards()

    # check for a blackjack or game over
    if user_score == 0 or comp_score == 0 or user_score > 21:
        game_over = True

    else:
        draw = input("Do you want to draw again? 'y' or 'n':\n")
        if draw == 'y':
            user_cards.append(deal_card())
            print_cards()
        elif draw == 'n':
            game_over = True


while comp_score < 17 and comp_score != 0:
    comp_cards.append(deal_card())
    comp_score = calculate_score(comp_cards)

print()
print("Your final hand: {}, final score: {}".format(
    user_cards, user_score))
print("Dealer's final hand: {}, final score: {}".format(
    comp_cards, comp_score))
print()

# print out the result and the final cards
print(compare(user_score, comp_score))
