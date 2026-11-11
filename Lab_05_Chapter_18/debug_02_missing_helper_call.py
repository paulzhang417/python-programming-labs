# debug 02 missing helper call
# Runestone Welcome to CS - Chapter 18
#
# EXERCISE 6 — Fix a Broken Composite Drawing (Debugging)
# The program should draw a square with a triangle on top.
# It currently draws only the square because the roof helper was not
# called, and the roof angle in draw_roof is wrong.
# Fix both problems; keep the design split into separate procedures.

import turtle

def draw_square(pen, size):
    pen.forward(size)
    pen.right(90)
    pen.forward(size)
    pen.right(90)
    pen.forward(size)
    pen.right(90)
    pen.forward(size)
    pen.right(90)

def draw_roof(pen, size):
    pen.left(90)
    pen.forward(size)
    pen.right(120)
    pen.forward(size)
    pen.right(120)
    pen.forward(size)
    pen.left(120)

def draw_house(pen, size):
    draw_square(pen, size)
    draw_roof(pen,size)
screen = turtle.Screen()
pen = turtle.Turtle()
draw_house(pen, 100)
screen.exitonclick()
