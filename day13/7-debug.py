#!/usr/bin/python3
"""Debug leap year exercise"""

# the year input is not converted to an integer
year = input("Which year do you want to check?: ")
# convert year to int
year = int(year)
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print(" Not Leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
