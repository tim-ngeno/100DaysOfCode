#!/usr/bin/env python3
"""Main module for the Pong game."""

from ball import Ball
from paddles import Paddle
from scores import Scores
from time import sleep
from turtle import Screen


# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


# Create the right paddle
right_paddle = Paddle()
right_paddle.goto(370, 0)

# Create the left paddle
left_paddle = Paddle()
left_paddle.goto(-370, 0)


# Initialize the ball
ball = Ball()


# Initialize scores
score = Scores()


# Listen for keyboard presses
screen.listen()

# Move the right paddle
screen.onkey(fun=right_paddle.move_up, key="Up")
screen.onkey(fun=right_paddle.move_down, key="Down")

# Move the left paddle
screen.onkey(fun=left_paddle.move_up, key="w")
screen.onkey(fun=left_paddle.move_down, key="s")


game_on = True
while game_on:
    sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_on_wall()

    # Detect collision with paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 350 or
            ball.distance(left_paddle) < 50 and ball.xcor() < -350):
        ball.bounce_on_paddle()

    # Detect when right_paddle misses
    if ball.xcor() > 380:
        ball.refresh()
        score.increase_l_score()

    # Detect when left_paddle misses
    if ball.xcor() < -380:
        ball.refresh()
        score.increase_r_score()

screen.mainloop()
