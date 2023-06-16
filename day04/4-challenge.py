import random

print("Using random module to choose who pays for the bill")
names = input("Give me everybody's names, separated by a comma.\n")

# Split the names into a list separated by commas
split_names = names.split(", ")

# get the number of items on the list using the len() function
length = len(split_names)

# randomise the list using the index of the items on it.
# subtract 1 because the index shifts from 0
choice = random.randint(0, length - 1)

# return the value of the random index
person_to_pay = split_names[choice]

print(f"{person_to_pay} is going to pay for the bill.")
