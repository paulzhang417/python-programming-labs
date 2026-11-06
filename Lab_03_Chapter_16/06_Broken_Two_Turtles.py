# Chapter 16 — Exercise 6: Broken Two Turtles
# Type: Debugging
#
# Correct the program so one red turtle draws a horizontal
# 100-pixel line starting at (-100, 50), while a blue turtle
# draws a vertical 100-pixel line starting at (100, -50).
#
# Expected: A red horizontal line and a blue upward vertical line
#

from turtle import *
red = Turtle()
blue = Turtle()
red.color("red")
blue.color("blue")
red.penup()
red.goto(-100, 50)
red.forward(100)
blue.penup()
blue.goto(100, -50)
blue.right(90)
blue.forward(100)
done()
