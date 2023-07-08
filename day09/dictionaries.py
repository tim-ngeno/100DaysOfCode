"""Dictionaries in python;
Data structures with key: value pairs"""

programming_dict = {
    "Bug": "An error in a piece of code that causes it to run unexpectedly",
    "Function": "A piece of code that can be called over and over",
    "Loop": "An action that is performed repeatedly over and over",
}
print("\n-----------------------------\n")
print(programming_dict)

print("\n-----------------------------\n")
# printing out a value for a key in a dictionary
print("printing out a value for a key in a dictionary")
print("result of Bug:\n", programming_dict["Bug"])
print("---------------------------------\n")

# adding an item to a dictionary
programming_dict["Dictionary"] = "A group of items stored as key-value pairs"
print(programming_dict)

# editing an item in a dictionary
programming_dict["Bug"] = "A moth in your computer"
print(programming_dict)

# wiping a dictionary
programming_dict = {}
print(programming_dict)

# NESTING

capital_cities = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting lists within a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

print()

# dictionaries within a dictionary
cities_visited = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 23
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 12
    },
}

print()
print(cities_visited["France"])

# Dictionaies within a list
travel_log = [
    {
        "country": "France",
        "visited": ["Paris", "Lille", "Dijon"],
        "visits": 23
    },
    {
        "Country": "Germany",
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
        "visits": 12
    },
]
