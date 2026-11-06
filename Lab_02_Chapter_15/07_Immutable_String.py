# Chapter 15 — Exercise 7: Immutable String
# Type: Debugging
#
# The programmer wants to change the first letter of "cat" to "b".
# Fix the program using slicing and concatenation, not index assignment.
# Print bat, while the original variable word remains cat.
#
# Expected: bat
#

word = "cat"
changed = word
changed[0] = "b"
print(changed)
