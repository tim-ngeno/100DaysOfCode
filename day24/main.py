#!/usr/bin/env  python3
"""Building the snake game"""

from time import sleep
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import ScoreBoard

# Setup the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

# Initialize the classes
snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


game_on = True
while game_on:
    screen.update()
    sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or
            snake.head.ycor() > 280 or snake.head.ycor() < -280):
        print("GAME OVER")
        score.set_high_score()
        snake.reset()

    # Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            score.set_high_score()
            snake.reset()

screen.exitonclick()
