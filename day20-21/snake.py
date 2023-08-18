#!/usr/bin/env python3
"""Defines the Snake module"""
from turtle import Turtle

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    """
    Snake Class that takes care of creating the snake and
    getting it to move on the screen
    """

    def __init__(self):
        """
        Initializes the snake with a snake body
        """
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        """
        Creates the snake body
        """
        positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in positions:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Adds a segment to the snake body
        """
        segment = Turtle(shape="square")
        segment.color("white")
        segment.shapesize(stretch_len=0.8, stretch_wid=0.8)
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        """
        Extends the snake on collision with food
        """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moves the snake segments"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)
        self.segments[0].forward(20)

    def up(self):
        """
        Turns the snake head upwards
        """
        # Make sure to use heading as a method
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Turns the snake head down
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        Turns the snake head to the left
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Turns the snake head to the right
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
