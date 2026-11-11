# exercise 03 robot face
# Runestone Welcome to CS - Chapter 18
#
# EXERCISE 3 — Decompose a Robot Face (Coding)
# Create a turtle drawing using these procedures:
#   draw_head(pen) — a rectangle outline 160 by 120
#   draw_eye(pen) — a filled circle of radius 12
#   draw_face(pen) — calls draw_head and draw_eye twice
# Start at the top-left corner of the head. Use penup/goto/pendown to
# position the eyes. Your draw_face procedure must CALL both helpers.
# Do not use loops.

import turtle

# Define draw_head, draw_eye, and draw_face here.

screen = turtle.Screen()
pen = turtle.Turtle()
# Call draw_face here.
screen.exitonclick()
