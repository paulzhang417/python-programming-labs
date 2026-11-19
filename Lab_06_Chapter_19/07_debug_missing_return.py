# Exercise 7 - Missing Return and Function Calls (Debugging)
# This program is supposed to print: Final price: 24.0
# It currently fails. Fix BOTH problems:
# 1. The discount function must return a number.
# 2. The final_price function must pass its computed value back.
# Keep the names and parameters unchanged.

def apply_discount(price, discount):
    price = price * (1 - discount)

def final_price(price, discount):
    result = apply_discount(price, discount)
    print(result)

amount = final_price(30, 0.20)
print("Final price:", amount)
