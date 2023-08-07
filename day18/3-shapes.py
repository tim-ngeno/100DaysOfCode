#!/usr/bin/env python3
"""Draw a bunch of shapes from square increasing in size to a
decagon"""

import random
from turtle import Turtle, Screen

colors = [
    "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
    "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"
]

t = Turtle()
t.speed(1)
for i in range(3, 11):
    t.color(random.choice(colors))
    for _ in range(i):
        t.pensize(2)
        t.forward(100)
        t.right(360 / i)


screen = Screen()
screen.exitonclick()
