#!/usr/bin/env python3
"""Off to the races!!"""

import random
from turtle import Turtle, Screen

screen = Screen()

# Resize the screen
screen.setup(width=500, height=400)

# turtle colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Prompt the user to make a bet
bet = screen.textinput(
    title="Make a bet",
    prompt="Which turtle will win the race? Enter a color: "
)

turtles = []

# beginning y position
y = 140

# Create the racing turtle instances
for i in range(0, 6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[i])
    t.goto(x=-200,  y=y)
    y -= 50
    turtles.append(t)

# Start the race
race_on = True

if bet:
    while race_on:
        for turtle in turtles:
            if turtle.xcor() > 220:
                race_on = False
                print("{} turtle is the winner".format(
                    turtle.pencolor()))
            # Move the turtles a random distance forward
            turtle.forward(random.randint(0, 10))

screen.exitonclick()
