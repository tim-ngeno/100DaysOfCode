#!/usr/bin/python3
"""Debugging"""

# 1.Describe the problem
"""
the below code uses the range() function to loop through numbers
1-20, the range() function, however, does not include the upper
bound of the number(s) passed, and hence `i` never gets to 20
"""


def my_function():
    for i in range(1, 20):
        if i == 20:  # if statement never gets evaluated
            print("You got it")


my_function()  # prints nothing

# FIXED CODE:


def my_fixed_function():
    for i in range(21):
        if i == 20:
            print("You got it")


my_fixed_function()
