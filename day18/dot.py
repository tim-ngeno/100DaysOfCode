import random
import turtle

t = turtle.Turtle()
turtle.colormode(255)


def random_color():
    """Generate a random color for turtle"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


for _ in range(1, 23):
    t.color(random_color())
    t.dot(10)
    t.forward(10)


t.screen.mainloop()
