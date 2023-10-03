#!/usr/bin/env python3
"""
*args and **kwargs
==================

args - contains an undefined number of positional arguments in a
    function
    - Args are of type tuple => '()'

kwargs -contains an undefined number of keyword arguments in a
    function
    - kwargs are natively of type dict => '{}'
"""


def add(*args):
    """
    Defines an add function that takes a variable number of arguments
    and returns the total sum of all the variables
    """
    return sum(args)


def calc(n, **kwargs):
    """
    Defines a function to perform mathematical operations using
    keyword arguments
    """
    for a in kwargs:
        print(a, kwargs[a])
    print(n)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


total = add(1, 2, 3, 4, 5, 6, 7)  # 28
print(total)

# **kwargs
calc(4, add=3, multiply=4)


class Car:
    """
    Creates a car with make and model

    Attributes:
        make (str): Make of the car
        model (str): model of the car
    """

    def __init__(self, **kw):
        """
        Initializes a car instance
        """
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan", model="GT-R")
print("Make: {}\nModel: {}".format(my_car.make, my_car.model))
