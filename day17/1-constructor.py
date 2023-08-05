#!/usr/bin/env python3
# using __init__ constructor

class Car:
    """Creates a car class"""

    def __init__(self, seats):
        """A constructor, initializes a car object with seats"""
        self.seats = seats

# Every object of the car class will be initialized with a required
# seat number


my_car = Car(5)
print(my_car.seats)


class User:
    """Defines a User class"""

    def __init__(self, id, username):
        """Initializes user object with id and username"""
        self.id = id
        self.username = username
        # adding default values
        self.followers = 0
        self.following = 0

    # Creating new methods
    def follow(self, user):
        """Follows a user account and increases count by 1"""
        user.followers += 1
        self.following += 1


bob = User("001", "bobby")
angela = User("002", "angela")

bob.follow(angela)
print(angela.followers)         # Should increase by 1
print(bob.id, bob.username)
