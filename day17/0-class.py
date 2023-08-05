#!/usr/bin/env python3
# creating classes with attributes

class User:
    """Defines an empty class User"""
    pass


# Creating attributes from the User class
user1 = User()
# user1 is an instance of the class User, meaning it is an object
# created from the User class

# ATTRIBUTES
# setting an attribute for a user object is simply defining a
# variable for that object, the difference is, we use the dot (`.`)
# notation to show that it belongs to `object`
user1.username = "Bob"

print(user1.username)
# Output = 'Bob'
