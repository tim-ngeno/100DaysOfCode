#!/usr/bin/env python3
"""The Hirst Painting project"""

import random
import turtle

colors = [
    (245, 243, 238), (246, 242, 244), (202, 164, 110),
    (240, 245, 241), (236, 239, 243), (149, 75, 50),
    (222, 201, 136), (170, 154, 41), (138, 31, 20),
    (134, 163, 184), (197, 92, 73), (145, 178, 149),
    (232, 176, 165), (160, 142, 158), (101, 75, 77)
]

# Create an instance of turtle
t = turtle.Turtle()
turtle.colormode(255)

# hide the pen to avoid tracing lines on our beautifullll painting
t.penup()
t.speed(10)
t.hideturtle()

# Get the turtle to the starting point
t.setheading(225)
t.forward(325)
t.setheading(0)

# Get the dots on the screen
for i in range(1, 101):
    t.dot(18, random.choice(colors))
    t.forward(50)

    if i % 10 == 0:
        # set the new-row-dots above previous row
        t.setpos(t.xcor(), t.ycor() + 50)
        t.left(90)
        t.left(90)
        t.forward(500)
        t.setheading(0)


# ANOTHER METHOD PERHAPS:
# while t.ycor() <= 210:
#     for _ in range(10):
#         color = random.choice(colors)
#         t.dot(16, color)
#         t.forward(50)

#     t.setpos(t.xcor(), t.ycor() + 50)
#     t.backward(400)


# Get the screen (canvas) object
screen = turtle.Screen()
screen.exitonclick()
