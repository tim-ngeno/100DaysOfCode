#!/usr/bin/env python3
"""The scores module"""

from turtle import Turtle


class Scores(Turtle):
    """
    This class manages the scores for the left and right
    players in the Pong game.

    Attributes:
        l_score (int): The score of the left player.
        r_score (int): The score of the right player.
    """

    def __init__(self):
        """
        Initializes the Scores class with initial scores of
        0 for both players.
        """
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_scores()

    def update_scores(self):
        """
        Updates the displayed scores on the screen.
        """
        self.clear()
        self.goto(-100, 250)
        self.write(
            "{}".format(self.l_score),
            align="center",
            font=("Cursive", 34, "normal")
        )
        self.goto(100, 250)
        self.write(
            "{}".format(self.r_score),
            align="center",
            font=("Cursive", 34, "normal")
        )

    def increase_l_score(self):
        """
        Increases the score of the left player by 1.
        """
        self.l_score += 1
        self.update_scores()

    def increase_r_score(self):
        """
        Increases the score of the right player by 1.
        """
        self.r_score += 1
        self.update_scores()
