products = [
    {"name": "Laptop", "price": 999.99, "category": "electronics", "in_stock": True},
    {"name": "Python Book", "price": 39.99, "category": "books", "in_stock": True},
    {"name": "Headphones", "price": 149.99, "category": "electronics", "in_stock": False},
    {"name": "Desk Lamp", "price": 29.99, "category": "home", "in_stock": True},
    {"name": "AI Textbook", "price": 89.99, "category": "books", "in_stock": True},
    {"name": "Monitor", "price": 349.99, "category": "electronics", "in_stock": True},
    {"name": "Notebook", "price": 4.99, "category": "office", "in_stock": True},
    {"name": "Keyboard", "price": 79.99, "category": "electronics", "in_stock": False},
]

in_stock = list(filter(lambda p: p["in_stock"], products))

discounted = list(map(
    lambda p: {**p, "discounted_price": round(p["price"] * 0.9, 2)}, products
))

cheap_electronics = [
    p for p in products
    if p["category"] == "electronics" and p["price"] < 200]

sorted_by_price = sorted(products, key=lambda p: p["price"])

from functools import reduce

total_value = reduce(
    lambda acc, p: acc + p["price"],
    filter(lambda p: p["in_stock"], products),
    0
)

grouped_by_category = reduce(
    lambda acc, p: {
        **acc, 
        p["category"]: acc.get(p["category"], []) + [p]
    },
    products,
    {}
)

print("Products with discounted_price:")
print(discounted)
print()

print("Electronics under $200:")
print(cheap_electronics)
print()

print("Products sorted by price:")
print(sorted_by_price)
print()

print("Total value of all in-stock products:")
print(total_value)
print()

print("Products grouped by category:")
print(grouped_by_category)
print()


