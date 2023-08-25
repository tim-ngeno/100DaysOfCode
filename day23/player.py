#!/usr/bin/env python3
"""The player module"""

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """
    Defines the player turtle class
    """

    def __init__(self):
        """
        Initializes the Player class
        """
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        """
        Moves the turtle upwards by a specified distance each time
        """
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        """
        Checks if the player has successfully reached the finish
        line

        Returns:
            True (bool): if the player crossed successfully
            False (bool): if the player hasn't crossed the finish
            line
        """
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False

    def go_to_start(self):
        """
        Get the player to go back to the start position
        """
        self.goto(STARTING_POSITION)
