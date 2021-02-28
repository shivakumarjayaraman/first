#!/usr/bin/env python3

import turtle
turtle.setup(500, 500)
window = turtle.Screen()
window.title("Event Handling 101")
window.bgcolor("lightblue")
nathan = turtle.Turtle()
def mf() :
    nathan.forward(50)

def ml() :
    nathan.left(30)

def mr() :
    nathan.right(30)

def start() :
    window.onkey(mf, "Up")
    window.onkey(ml, "Left")
    window.onkey(mr, "Right")
    window.listen()
    window.mainloop()

if __name__ == "__main__" :
    start()
