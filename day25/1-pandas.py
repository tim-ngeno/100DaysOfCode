#!/usr/bin/env python3
"""Using pandas to read csv data"""

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])
