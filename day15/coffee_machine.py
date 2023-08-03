"""Make a coffee machine-ish"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def print_report():
    """
    Formats the resources into a readable output
    and prints a report
    """
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = profit
    print("Water: {}ml\nMilk: {}ml\nCoffee: {}g\nMoney: ${}"
          .format(water, milk, coffee, money))


def resources_sufficient(order):
    """
    Checks if resources are sufficient to make the order

    Args:
        order (str): user's drink order
    Returns:
        True (bool): if resources are enough to make order
        False (bool): if resources are insuffient
    """
    order_item = MENU[order]["ingredients"]
    for ingredient in order_item:
        if resources[ingredient] < order_item[ingredient]:
            print("Sorry there isn't enough {}".format(ingredient))
            return False
        return True


def process_coins(order):
    """
    Calculates the amount paid for coffee and optionally
    return balance
    """
    print("\nThat will be ${}. Insert coins:".format(
        MENU[order]["cost"]))
    quarters = float(input("Quarters: ")) * 0.25
    dimes = float(input("Dimes: ")) * 0.1
    nickels = float(input("Nickels: ")) * 0.05
    pennies = float(input("Pennies: ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return round(total, 2)


def transaction(drink):
    """
    Checks if amount paid is sufficient to buy coffee order

    Args:
        drink: drink order
    Returns:
        True: if transaction is successful
        False: if transaction fails(amount paid is not enough)
    """
    global profit

    amount_paid = process_coins(drink)
    if MENU[drink]["cost"] < amount_paid:
        bal = amount_paid - MENU[drink]["cost"]
        profit += amount_paid - bal
        print("Here's ${} in change".format(round(bal, 2)))
        return True
    elif MENU[drink]["cost"] == amount_paid:
        return True
    else:
        print("Sorry that's not enough money. Refunded.")
        return False


def make_coffee(coffee_order):
    """
    Makes requested coffee order and updates resources used
    """
    coffee = MENU[coffee_order]["ingredients"]
    for ingredient in coffee:
        resources[ingredient] -= coffee[ingredient]
    print("Here's your {}☕. Enjoy!".format(coffee_order))


machine_on = True
prompt = "\nWhat would you like?(espresso/latte/cappuccino)\n"
while machine_on:
    choice = input(prompt).lower()

    if choice == 'off':
        # turn off the machine
        machine_on = False
    elif choice == 'report':
        # print report on available resources
        print_report()
    else:
        try:
            if resources_sufficient(choice):
                if transaction(choice):
                    make_coffee(choice)
        except KeyError:
            print("{} is not on the menu".format(choice))
