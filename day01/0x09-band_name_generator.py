# Create a band name generator
import time

print("Welcome to the Band Name Generator\n")
city = input("What is the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("\nGenerating a cool band name...")
time.sleep(2)
print("The " + city.capitalize() + " " + pet.capitalize() + "s")
