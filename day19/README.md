# Python Higher Order Functions and Event Listeners
Python Higher Order functions are functions that take other functions as arguments:
```
def add(a, b):
    return(a + b)

def calculator(a, b, add):
    add(a, b)
```
In this example, the function `calculator()` is a higher order function, since it takes the function `add` as input and uses it to, well, add...

Notice that the `add()` function is used without the parentheses, this is because adding the parentheses will invoke the method and execute it at that point, but that doesn't give the expected result.

Higher Order Functions are useful when listening for events, this way a function can be tied up to a specific key binding, for example.

## Object State and Instances
An object is an instance of a class. We can have multiple instances from the same class

```
from turtle import Turtle

# This is a turtle object called turtle_a
turtle_a = Turtle()

# This is another turtle object, called turtl_b
turtle_b = Turtle()
```

From the above code, `turtle_a` and `turtle_b` are both instances from the Turtle class. This means that they are independent from each other, they can have different color, shape, and other attributes.
