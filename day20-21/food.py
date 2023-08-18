#!/usr/bin/env python3
"""Defines the snake food module"""

import random
from turtle import Turtle


class Food(Turtle):
    """
    Defines the snake's food from the Turtle Class
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        """
        Moves the snake food to a new random location on collision
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
