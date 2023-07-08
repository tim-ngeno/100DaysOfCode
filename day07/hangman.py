import random
print("Welcome to the hangman game!")

word_list = ['advark', 'baboon', 'camel', 'ammend', 'involve',
             'modicum,', 'respect', 'wanton', 'lethargic',
             'minefield', 'minerals', 'syllogism', 'import', 'brainwash']

# randomly choose a word from the list and assign it to a variable called chosen_word

chosen_word = random.choice(word_list)

# print(f"The word is {chosen_word}")

# Create an empty list called display. For each letter in the chosen_word, add an "_" to display.

display = []
for n in range(0, len(chosen_word)):
    display += "_"
# 3# loop through each position in the chosen word;
# if the letter at the position matches 'guess', then reveal that letter in the display at that position.

end_of_game = False
lives = 8
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}. Be a little creative!")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word. You lose a life.")
        print(f"{lives} lives remaining")
        if lives == 0:
            end_of_game = True
            print('You lose')

    print(f"{' '.join(display)}\n")

    if "_" not in display:
        end_of_game = True
        if lives < 2:
            print('Oooof! Close one!')
        else:
            print("Nice going. You win!")
