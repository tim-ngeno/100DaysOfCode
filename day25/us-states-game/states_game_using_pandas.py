"""The US States Guessing Game Using pandas Library"""

# This program lets the user guess the names of all 50 US states
# using the pandas library.


import pandas
import turtle

# Initialize the turtle screen and load the blank map image.
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read data from the csv file and store it in a DataFrame.
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

# Initialize the lists of guessed states and states to learn.
guessed_states = []
states_to_learn = []
score = 0

# Keep looping until the user has guessed all 50 states.
while len(guessed_states) < 50:
    # Get the user's guess.
    answer_state = turtle.textinput(
        title="{}/50 States".format(score),
        prompt="Guess a state"
    ).title()

    # Check if the guess is correct.
    if answer_state in states:
        # Write the correct guess on the map.
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(state_data.state.item())
        score += 1

    # If the user quits the game, save the list of states to learn.
    if answer_state == "Exit":
        for state in states:
            if state not in guessed_states:
                states_to_learn.append(state)
        df = pandas.DataFrame(states_to_learn)
        df.to_csv("missed_states.csv")
        break

# Exit the program.
screen.mainloop()
