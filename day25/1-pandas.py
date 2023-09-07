#!/usr/bin/env python3
"""Using pandas to read csv data"""

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])             # same as print(data.temp)


# Convert the data to a dict
data_dict = data.to_dict()
print("\nPandas dataframe to dict:\n", data_dict)

# get a list of temperatures
temp_list = data["temp"].to_list()
print("\nTemperatures list: {}".format(temp_list))


# Average temperature
avg_temp = sum(temp_list) / len(temp_list)
print("\nAverage temperature: {}".format(avg_temp))

# with pandas
print(data["temp"].mean())

# Get the maximum temp
print(data["temp"].max())
print(data.temp)


# Get the ROWS!!
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])


# Being specific with row values
monday = data[data.day == "Monday"]
print(monday.condition)

print((monday.temp * 9/5) + 32)
