#!/usr/bin/env python3
"""Create the etch-a-sketch game"""

from turtle import Turtle, Screen

t = Turtle()


def move_forwards():
    """
    Moves the turtle object forwards
    """
    t.forward(10)


def move_backwards():
    """
    Moves the turtle backwards
    """
    t.backward(10)


def turn_right():
    """
    Turns the turtle in the clockwise direction
    """
    t.right(20)


def turn_left():
    """
    Turns the turtle in the counter-clockwise direction
    """
    t.left(20)


def clear_screen():
    """
    Clears the turtle drawings on screen and sets the
    turtle back hom
    """
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen = Screen()
screen.listen()

screen.onkey(fun=move_forwards, key='w')
screen.onkey(fun=move_backwards, key='s')
screen.onkey(fun=turn_left, key='a')
screen.onkey(fun=turn_right, key='d')
screen.onkey(fun=clear_screen, key='c')

screen.exitonclick()
