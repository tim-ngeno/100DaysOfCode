#!/usr/bin/env python3
import pandas

data = pandas.read_csv("squirrel_data.csv")

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrels, red_squirrels, black_squirrels)

squirrels = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels],
}

df = pandas.DataFrame(squirrels)

with open("squirrel_count.csv", "w") as file:
    file.write(df.to_csv())
