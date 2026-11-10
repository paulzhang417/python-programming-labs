# debug 02 parameter order
# Runestone Welcome to CS - Chapter 17
#
# EXERCISE 6 — Fix Parameter Order (Debugging)
# This code is supposed to print:
# Area: 40
# Area: 21
# The current calculation uses the wrong operation and the second call
# has the wrong number of arguments. Fix both errors.

def show_area(width, height):
    area = width + height
    print("Area: " + str(area))

show_area(8, 5)
show_area(7)
