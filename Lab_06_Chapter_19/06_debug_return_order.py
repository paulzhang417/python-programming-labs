# Exercise 6 - Return Ends a Function (Debugging)
# This program should add 5 to the score, but prints the wrong result.
# Fix the function so the output is exactly: Score: 15
# You may change the function body. Keep the function name and call.
# Explain in one comment why the original code was wrong.

def add_five(x):
    return x
    x = x + 5

score = 10
score = add_five(score)
print("Score:", score)
