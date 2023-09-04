#!/usr/bin/env python3
"""Read data from a csv file"""

import csv

# Without csv module
with open("weather_data.csv", "r") as csv_file:
    content = csv_file.read().splitlines()
    # print(content)


# With csv module
with open("weather_data.csv", "r") as file:
    data = csv.reader(file)     # creates a csv object
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(temperatures)
