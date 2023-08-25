#!/usr/bin/env python3
"""The scoreboard module"""
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """
    Defines the Scoreboard class for handling scores of player
    """

    def __init__(self):
        """
        Initializes the scoreboard
        """
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-270, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Updates the current level the player is at
        """
        self.clear()
        self.write(
            "Level: {}".format(self.level),
            align="left",
            font=FONT
        )

    def increase_level(self):
        """
        Increases level after player crosses successfully
        """
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """
        Handles the game over sequence
        """
        self.home()
        self.write("GAME OVER", align="center", font=FONT)
