#!/usr/bin/python3
"""Debugging"""

number = int(input("Which number do you want to check?: "))

"""The bug in the code is in the if statement, where an assignment
operator is used to check for equality

Use a double equals '==' operator
"""

# if number % 2 = 0:
if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")
