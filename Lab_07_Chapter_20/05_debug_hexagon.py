# Chapter 20 - Exercise 5: Debug a Polygon
# This program should draw a CLOSED regular hexagon with 6 sides,
# each of length 70, and print Done only once.
# It has TWO logical errors. Correct them without removing the loop.
import turtle
pen = turtle.Turtle()
for side in range(5):
    pen.forward(70)
    pen.right(90)
print("Done")
