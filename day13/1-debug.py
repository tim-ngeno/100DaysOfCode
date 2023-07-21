#!/usr/bin/python3
"""Debugging"""

# 2. Reproduce the problem


"""The randint method from random picks a random number between
1(inclusive) and 6(inclusive)

Our list, however, is 0-indexed, indexing begins from 0, and goes ti
len(numbers) - 1, which is 6. On occasion therefore, when the random
number generated is 6, the program throws a IndexError
"""


from random import randint
numbers = [1, 2, 3, 4, 5, 6]
n = randint(1, 6)
print(numbers[n])

# the proper range
n = randint(0, 5)
