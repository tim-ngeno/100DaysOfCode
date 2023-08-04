from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()

machine_is_on = True
while machine_is_on:
    options = menu.get_items()
    prompt = f"What would you like? {options}\n"
    choice = input(prompt).lower()
    if choice == 'off':
        machine_is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if (coffee_maker.is_resource_sufficient(drink) and
                money.make_payment(drink.cost)):
            coffee_maker.make_coffee(drink)
