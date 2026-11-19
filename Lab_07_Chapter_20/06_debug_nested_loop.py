# Chapter 20 - Exercise 6: Debug a Nested Loop
# Goal: Draw 3 squares, each rotated 120 degrees from the previous.
# Every square must have 4 sides of length 60.
# Fix the TWO logic mistakes in the loops/turns.
import turtle
pen = turtle.Turtle()
for shape in range(3):
    for side in range(3):
        pen.forward(60)
        pen.right(90)
    pen.right(90)
