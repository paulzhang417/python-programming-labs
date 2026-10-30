# LAB 01 - DEBUG 2: STORE INVOICE
# A shop sells 3 notebooks at $4 each and 2 pens at $2 each.
# Sales tax is 13%.
# Fix THREE mistakes so the subtotal, tax, and total are correct.
# Expected output:
# Subtotal: 16
# Tax: 2.08
# Total: 18.08

notebook_price = 4
notebook_quantity = 3
pen_price = 2
pen_quantity = 2
tax_rate = 0.13

subtotal = notebook_price + notebook_quantity + pen_price * pen_quantity
tax = subtotal * 13
total = subtotal - tax
print("Subtotal:", subtotal)
print("Tax:", round(tax, 2))
print("Total:", round(total, 2))
