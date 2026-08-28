item1_name = "Notebook"
item1_price = "4.99"
item1_qty = "2"

item2_name = "Pen Pack"
item2_price = "7.50"
item2_qty = "1"

item3_name = "Backpack"
item3_price = "34.99"
item3_qty = "1"

tax_rate = "0.075"

price1 = float(item1_price)
qty1 = int(item1_qty)

price2 = float(item2_price)
qty2 = int(item2_qty)

price3 = float(item3_price)
qty3 = int(item3_qty)

tax = float(tax_rate)

# Line totals
line1 = price1 * qty1
line2 = price2 * qty2
line3 = price3 * qty3

# Subtotal
subtotal = line1 + line2 + line3

# Tax amount
tax_amount = subtotal * tax

# Grand total
grand_total = subtotal + tax_amount

# Print formatted receipt
print("========================================")
print("              STORE RECEIPT")
print("========================================")

print(f"{item1_name:<15} ${price1:.2f} x {qty1:<3} ${line1:.2f}")
print(f"{item2_name:<15} ${price2:.2f} x {qty2:<3} ${line2:.2f}")
print(f"{item3_name:<15} ${price3:.2f} x {qty3:<3} ${line3:.2f}")

print("----------------------------------------")
print(f"Subtotal:{'':>22}${subtotal:.2f}")
print(f"Tax (7.5%):{'':>20}${tax_amount:.2f}")
print("========================================")
print(f"TOTAL:{'':>25}${grand_total:.2f}")
print("========================================")