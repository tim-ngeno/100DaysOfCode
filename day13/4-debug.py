"""Debugging"""

# 5. Print is Your Friend

"""
The bug in this code is that the == operator is used on a variable
that takes input from the user

Use print statements to see what's happening
"""

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))

# use print to evaluate the variable values
print("Pages =", pages)
print("Words per page =", word_per_page)
# The double equal operator evaluates the value of word_per_page
# with the input expected from the user, which evaluates to False
# The correct way would be to use an assignment operator instead

print("\nAfter fix:\n")
word_per_page = int(input("Number of words per page: "))
print("Words per page=", word_per_page)
total_words = pages * word_per_page
print("Total words: {}".format(total_words))
