"""Create the scoreboard module"""

from turtle import Turtle

FONT_FORMAT = ("Cursive", 18, "normal")


class ScoreBoard(Turtle):
    """
    Defines a class to keep track of user scores
    """

    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("high_score.txt", "r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        """
        Updates the score with the current score
        """
        self.clear()
        self.write("SCORE: {}  High Score: {}".format(
            self.score, self.high_score),
            align="center", font=(FONT_FORMAT)
        )

    def increase_score(self):
        """
        Increases the score when snake collides with the food
        """
        self.score += 1
        self.update_score()

    def set_high_score(self):
        """
        Sets the highest score as the new high score
        """
        if self.score > self.high_score:
            self.high_score = self.score
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def game_over(self):
        """
        Handles the game over sequence
        """
        self.home()
        self.write("GAME OVER.", align="center",
                   font=(FONT_FORMAT))
