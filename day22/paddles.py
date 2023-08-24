#!/usr/bin/env python3
"""The paddles module"""

from turtle import Turtle


class Paddle(Turtle):
    """
    This class represents the paddles used in the Pong game.
    """

    def __init__(self):
        """
        Initializes the Paddle class instance.
        """
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        """
        Creates a paddle object.
        """
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)

    def move_up(self):
        """
        Moves the paddle object upwards.
        """
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        """
        Moves the paddle object downwards.
        """
        self.goto(self.xcor(), self.ycor() - 20)
