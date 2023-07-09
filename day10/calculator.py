"""Implement a simple calculator"""


def add(n1, n2):
    """adds two numbers n1 and n2 and returns the sum
    Args:
        n1 (int): the first argument
        n2 (int): the second argument
    """
    return n1 + n2


def subtract(n1, n2):
    """subtracts two numbers n1 and n2 and returns the difference
    Args:
        n1 (int): the first argument
        n2 (int): the second argument
    """
    return n1 - n2


def multiply(n1, n2):
    """multiplies n1 and n2 and returns the product
    Args:
        n1 (int): the first argument
        n2 (int): the second argument
    """
    return n1 * n2


def divide(n1, n2):
    """divides n1 and n2 and returns the result
    Args:
        n1 (int): the first argument
        n2 (int): the second argument
    """
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    """Performs simple mathematical calculations

    Args:
        num1 (int/float): first input number
        symbol (str): calculation symbol like '+', '-'
        num2 (int/float): the next number in the calculation
        result (int/float): the result of the calculation

    Return:
        Result of the calculation in specified format
    """
    num1 = float(input("\nWhat is the first number:\n"))
    for key in operations:
        print(key)

    should_continue_op = True
    while should_continue_op:
        # display and get operation input
        symbol = input("Pick an operation:\n")
        if symbol not in operations:
            print("INVALID OPERATION!")
            calculator()
        num2 = float(input("What is the next number:\n"))

        calc_func = operations[symbol]
        result = calc_func(num1, num2)
        print("{} {} {} =".format(num1, symbol, num2), result)

        new = input(
            "'y' to continue with {}, 'n' to start, 'x' to exit\n".format(result))
        if new == 'y':
            num1 = result
        elif new == 'n':
            calculator()
        elif new == 'x':
            exit()
        else:
            print("bye...")
            should_continue_op = False


calculator()
