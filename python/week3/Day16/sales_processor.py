from functools import reduce
sales = [
    {"product": "Laptop", "price": 60000},
    {"product": "Mouse", "price": 800},
    {"product": "Keyboard", "price": 1500},
    {"product": "Monitor", "price": 12000},
    {"product": "Headphones", "price": 2500}
]

product_name = list(
    map(lambda x: x["product"],sales)
)
print("Product Name :",product_name)

more_5k = list(
    map(lambda x: x["product"], filter(lambda x: x["price"] > 5000, sales))
)
print("Costing more than 5k :",more_5k)

total_sales = reduce(lambda a, b: a + b["price"],sales, 0)
print("Total Sales :",total_sales)

discount = list(
    map(lambda x: {"product": x["product"], "price": x["price"] * 0.90},sales)
)
print("10% Discount :",discount)

discount_5k = list(
    map(lambda x: x["product"], filter(lambda x: x["price"] > 5000, discount))
)
print("Still costing more than 5k after discunt :",discount_5k)