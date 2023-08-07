#!/usr/bin/env python3
"""Use Turtle graphics to draw a square"""

from turtle import Turtle, Screen

t = Turtle()
t.shape("turtle")
t.color("blue")

# Draw a square
for _ in range(4):
    t.forward(100)
    t.left(90)

screen = Screen()
screen.exitonclick()
