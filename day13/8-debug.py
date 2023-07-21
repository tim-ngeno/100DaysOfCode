#!/usr/bin/python3
"""Debug the fizzbuzz problem"""

for number in range(1, 101):
    # 1. first bug: uses the OR operator insted of AND: number needs
    # to be divisible by both 3 and 5

    # 2. Using nested if statements instead of nested if..elif..else

    # if number % 3 == 0 or number % 5 == 0: #bug
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
