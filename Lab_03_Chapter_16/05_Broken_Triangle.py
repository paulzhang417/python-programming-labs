# Chapter 16 — Exercise 5: Broken Triangle
# Type: Debugging
#
# Fix the turtle commands so the program draws a closed
# equilateral triangle with side length 100.
# There are two incorrect turns and a misspelled turtle method.
#
# Expected: Closed equilateral triangle
#

from turtle import *
artist = Turtle()
artist.forward(100)
artist.left(90)
artist.forward(100)
artist.left(90)
artist.forword(100)
done()
