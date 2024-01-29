#!/usr/bin/env python3
"""Flash Card Program to learn popular French words"""

import pandas as pd
import random
import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"

# Load data from CSV file or use default French words file
try:
    content = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    content = pd.read_csv('data/french_words.csv')

data = content.to_dict(orient='records')
current_card = {}


def next_card():
    """
    Generates French words from the CSV data file and updates the
    flash card.
    """
    global current_card, flip_timer
    current_card = random.choice(data)
    window.after_cancel(flip_timer)
    update_card('French', 'black', card_front)

    # Schedule flipping the card after 3000 milliseconds
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """
    Flips the card to display the English translation of the current
    French word.
    """
    update_card('English', 'white', card_back)


def known_words():
    """
    Removes the word marked as known from the list of cards.
    """
    data.remove(current_card)
    to_learn = pd.DataFrame(data)
    to_learn.to_csv('data/words_to_learn.csv', index=False)
    next_card()


def update_card(title_text, text_fill, bg_image):
    """
    Updates the flash card with the specified parameters.
    """
    canvas.itemconfig(card_title, text=title_text, fill=text_fill)
    canvas.itemconfig(card_word, text=current_card[title_text], fill=text_fill)
    canvas.itemconfig(card_background, image=bg_image)


# Create the main window
window = tk.Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Flip the card after 3 seconds
flip_timer = window.after(3000, func=flip_card)

# Setup the canvas
canvas = tk.Canvas(width=800, height=526)
card_front = tk.PhotoImage(file='images/card_front.png')
card_back = tk.PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(
    400, 150, text='', font=('Arial', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=('Arial', 50, 'bold'))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Setup and define buttons
cross_image = tk.PhotoImage(file='images/wrong.png')
cross_button = tk.Button(
    image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=0)

check_image = tk.PhotoImage(file='images/right.png')
check_button = tk.Button(
    image=check_image, highlightthickness=0, command=known_words)
check_button.grid(row=1, column=1)

next_card()

window.mainloop()
