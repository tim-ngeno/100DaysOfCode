#!/usr/bin/env python3
"""Create a Random Walk"""
import random
import turtle

t = turtle.Turtle()
turtle.colormode(255)


def random_color():
    """Generates a random RGB sequence color for our turtle"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


pos = [90, 180, 270, 360]
t.pensize(4)
t.speed("fastest")

for _ in range(500):
    t.color(random_color())
    t.forward(20)
    t.setheading(random.choice(pos))

screen = turtle.Screen()
screen.exitonclick()
