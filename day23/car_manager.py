#!/usr/bin/env python3
"""The cars module"""

import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    """
    Defines the CarManager module used to create the random
    cars for the game
    """

    def __init__(self):
        """
        Initializes the CarManager class with random car objects
        """
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """
        Creates a car instance on the screen
        """
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(stretch_len=2, stretch_wid=1)
            random_y_pos = random.randint(-250, 250)
            car.goto(300, random_y_pos)
            self.all_cars.append(car)

    def move_car(self):
        """
        Moves the car instance on the screen
        """
        for car in self.all_cars:
            car.setheading(180)
            car.forward(self.car_speed)

    def level_up(self):
        """
        Increase the cars' speed when user completes new level
        """
        self.car_speed += MOVE_INCREMENT
