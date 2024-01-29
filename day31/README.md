# Flashy - French Vocabulary Flash Card Program

Flashy is a simple yet effective program designed to help users learn popular French words through flashcards. The program allows users to review and test their knowledge of French-English translations in an interactive and engaging way.

## Features

1. **Dynamic Learning:** Flashy uses a CSV file containing French and English word pairs to generate flashcards dynamically. Users can start learning immediately or add new words to the dataset.

2. **Intuitive Interface:** The program features a user-friendly interface where users can flip cards to reveal the English translation of the displayed French word.

3. **Mark Words as Known:** Users can mark words they already know, and these words will be removed from the active list, ensuring focus on words that need more attention.

4. **Persistence:** Flashy saves the progress by updating the dataset and removing known words. The progress is stored in a CSV file for future use.

## Getting Started

1. Ensure you have Python installed on your system.
2. Install required dependencies using `pip install pandas`.
3. `cd` into the `FlashCard` directory
4. Run the program using `python3 main.py`.

## How to Use

1. **Start Learning:** Upon running the program, it will display a French word. After a few seconds, the card flips to reveal the English translation.

2. **Mark as Known:** If you know the word, click the checkmark button. Flashy will remove the word from the active list.

3. **Next Word:** If you want to skip or mark a word as unknown, click the X button to move to the next word.

4. **Persistence:** Your progress is automatically saved. You can resume learning where you left off the next time you run the program.

## Customization

- Users can customize the word dataset by modifying the CSV file.
- Additional French-English word pairs can be added to the dataset.

## Dependencies

- [Pandas](https://pandas.pydata.org/): Used for data manipulation and CSV file handling.

## Credits

This program is inspired by language learning flashcard techniques and utilizes the power of Python and the Tkinter library for the graphical user interface.

Feel free to contribute, suggest improvements, or report issues!

Happy Learning!
