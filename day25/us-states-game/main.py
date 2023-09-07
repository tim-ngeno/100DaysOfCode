"""
The US States Guessing Game

This is a game in which the user is presented with the map of the
United States of America and the player has to guess the states. If
the user guess is correct, the name of the state is placed in the
correct position on the map

"""


import turtle

# Initialize the turtle screen and load the blank map image.
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read the list of US states from a CSV file.
with open("50_states.csv", "r") as file:
    data = file.read().splitlines()

# Initialize the lists of correct guesses and states to learn.
correct_guesses = []
states_to_learn = []
score = 0

# Keep looping until the user has guessed all 50 states.
while len(correct_guesses) < 50:
    # Get the user's guess.
    answer_state = screen.textinput(
        title="{}/50 Correct".format(score),
        prompt="Guess a state name"
    ).title()

    # Check if the guess is correct.
    if answer_state in data[1:]:
        # Write the correct guess on the map.
        writer = turtle.Turtle()
        writer.penup()
        writer.hideturtle()
        writer.goto(int(data[data.index(answer_state)][1]),
                    int(data[data.index(answer_state)][2]))
        writer.write("{}".format(answer_state))
        correct_guesses.append(answer_state)
        score += 1

    # If the user quits the game, save the list of states to learn.
    if answer_state == "Exit":
        for state in data[1:]:
            state_name = state.split(",")[0]
            if state_name not in correct_guesses:
                states_to_learn.append(state_name)
        with open("states_to_learn", "w") as file:
            for name in states_to_learn:
                file.write("{}\n".format(name))
        break

# Exit the program.
screen.mainloop()
