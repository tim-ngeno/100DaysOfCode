#!/usr/bin/env python3

"""Creating a dataframe from python native data types"""

import pandas

students = {
    "Pupils": ["Amy", "Jane", "Gill"],
    "Marks": [76, 87, 56]
}

# Create a pandas DataFrame
data = pandas.DataFrame(students)
print(data)

with open("students.csv", "w") as file:
    file.write(data.to_csv())
