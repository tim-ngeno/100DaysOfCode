# Create a global variable
balls = 1


def increase_balls():
    """Defines a local variable `balls`"""
    balls = 2
    print("balls inside function: {}".format(balls))


increase_balls()
print("balls outside function: {}".format(balls))


# MODIFYING GLOBAL SCOPE
# TO MAKE GLOBAL VARIABLES INSIDE FUNCTIONS, USE THE `global` KEYWORD

def mod_increase_balls():
    """
    Modified version of increase_balls that
    uses the global variable
    """
    global balls
    balls += 1
    print("balls inside modified function: {}".format(balls))


mod_increase_balls()
