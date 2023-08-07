#!/usr/bin/env python3
"""Draw a spirograph"""

import random
import turtle


def random_color():
    """Generates a random rgb color for turtle"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# Create an instance of Turtle
t = turtle.Turtle()

# Set color mode to 255 to use rgb colors
turtle.colormode(255)

t.speed("fastest")

angle = 20
for i in range(int(360 / 5)):
    t.color(random_color())
    t.setheading(angle)
    t.circle(100)
    angle += 5


screen = turtle.Screen()
screen.exitonclick()
