#!/usr/bin/env python3

import turtle

t = turtle.Turtle()

t.color("red")
t.fillcolor("yellow")

t.begin_fill()
while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos()) < 1:
        break

t.end_fill()

t.screen.mainloop()
