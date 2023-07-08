"""Using functions with keyword arguments
:: Calculate how much paint is needed"""

# number of cans = (height * width) / coverage
import math


def paint_calc(height, width, cover):
    """Defines a function to calculate how much
    paint is needed per square area of a wall
    Args:
        height (int, float): height of the wall
        width (int, float): width of the wall
        cover (int): coverage
    """
    number_of_cans = math.ceil((test_height * test_width) / cover)
    print(f"You'll need {number_of_cans} cans of paint")


test_height = int(input("Height of wall:  "))
test_width = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_height, width=test_width, cover=coverage)
