#!/usr/bin/env python3
"""The ball module"""

import random
from turtle import Turtle


class Ball(Turtle):
    """
    This class represents the ball in the Pong game.

    Attributes:
        ball_speed (float): The speed at which the ball moves.
    """

    def __init__(self):
        """
        Initializes the Ball class and places the ball on the screen.
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x = 10
        self.y = 10
        self.ball_speed = 0.05

    def move(self):
        """
        Move the ball on the screen.
        """
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_on_wall(self):
        """
        Bounce the ball on collision with top/bottom walls.
        """
        self.y *= -1

    def bounce_on_paddle(self):
        """
        Bounce the ball on collision with a paddle.
        """
        self.x *= -1
        self.ball_speed *= 0.9

    def refresh(self):
        """
        Resets the ball's position and properties when a player misses.
        """
        self.home()
        self.x *= -1
        self.ball_speed = 0.1
