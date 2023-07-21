#!/usr/bin/python3
"""Debugging"""

# 3. Play computer

"""The bug in this code is that if 1994 is the input year, nothing
is printed. Clearly we want millenials born in 1994 to know
themselves, oldies!

The program evaluates the years between 1980 and 1994, just as that:
it does not include the upper and lower bounds

To include the year 1980 and 1994, the operator should be changed to
<= and >=, respectively
"""

year = int(input("What's your year of birth?: "))
# if year > 1980 and year < 1994: # the bug
if year >= 1980 and year <= 1994:
    print("You are a millenial")
elif year > 1994:
    print("You are a gen-z")
