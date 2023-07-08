"""Functions with parameters"""


def greet():
    """A simple function that prints a greeting to the user"""
    print("greet 1")
    print("greet 2")
    print("greet 3")


greet()


def greet_with_name(name):
    """Print greeting to the user followed by their name
    Args:
        name (str): name of person to be greeted
    """
    print(f"Hello, {name}")
    print(f"How do you do, {name}?")


greet_with_name("Angela")


# Function with more than one parameter

def greet_with(name="Jack Bauer", location=""):
    """Function with more than one parameter
    Shows the use of positional and keyword arguments
    Args:
        name (str): first keyword argument that takes name of user
        location (str): second keyword argument, location of user
    Return:
        prints greeting and asks about weather in `location`
    """
    print(f"Hello, {name}")
    print(f"What is it like in {location}?")


greet_with("Tim", "France")
