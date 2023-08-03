#!/usr/bin/env python3
# Using packages to simplify functionality
# PrettyTable is a package that prints output in table format,
# making it more readable for the user

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle",
                                  "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"               # left align
print(table)
