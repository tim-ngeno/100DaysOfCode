#!/usr/bin/python3
import random
from word_list import word_list
from stages_art import stages

print("Welcome to the hangman game")

# pick a random word from list of words
choice_word = random.choice(word_list)
print(f"Your word has {len(choice_word)} letters")

lives = 6
display = []
for _ in range(0, len(choice_word)):
    display += "_"

game_over = False
while not game_over:
    guess = input("\nGuess a letter: ")

    for pos in range(len(choice_word)):
        letter = choice_word[pos]
        if guess == letter:
            display[pos] = guess
    if guess not in choice_word:
        lives -= 1
        print(f"{guess} not in word. You lose a life")
        print(stages[lives])
        print(f"{lives} lives remaining\n")
        if lives == 0:
            print("You ran out of lives. GAME OVER!")
            game_over = True

    print(f"{' '.join(display)}")
    if "_" not in display and lives != 0:
        print("You won!")
        game_over = True
