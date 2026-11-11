# debug 01 procedure order
# Runestone Welcome to CS - Chapter 18
#
# EXERCISE 5 — Fix Procedure Order (Debugging)
# This should draw two squares side-by-side using a helper procedure.
# It currently tries to use a procedure before it is defined.
# Change the order so that all procedure definitions run BEFORE they
# are called, without duplicating the drawing code.

import turtle

screen = turtle.Screen()
pen = turtle.Turtle()
draw_two_squares(pen)

def draw_square(pen, size):
    pen.forward(size)
    pen.right(90)
    pen.forward(size)
    pen.right(90)
    pen.forward(size)
    pen.right(90)
    pen.forward(size)
    pen.right(90)

def draw_two_squares(pen):
    draw_square(pen, 60)
    pen.penup()
    pen.forward(100)
    pen.pendown()
    draw_square(pen, 60)

screen.exitonclick()
