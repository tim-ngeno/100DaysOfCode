#!/usr/bin/python3
"""Debugging"""

# 4. Fix the Errors!
"""The error you run into when executing this program is the
TypeError

The input function gets the user input as a string, and we're trying
to use the > operator to compare a number (type int) and a string
(type str)

We should therefore cast the value of age into an integer before
doing the comparison
"""

# age = input("How old are you?: ") # the buggy line
age = int(input("How old are you?: "))  # the fix
if age > 18:
    print("You can drive")
