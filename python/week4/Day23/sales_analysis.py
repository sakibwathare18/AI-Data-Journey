import numpy as np

sales = np.array([
    [1200, 1500, 1700, 1600],
    [900, 1100, 1250, 1300],
    [2000, 2200, 2100, 2400],
    [1500, 1600, 1550, 1700]
])

# 1. Calculate sum for each product (across columns)
product_totals = np.sum(sales, axis=1)

# 2. Calculate sum for each month (across rows)
monthly_totals = np.sum(sales, axis=0)

# 3. Calculate average for each product (across columns)
product_averages = np.mean(sales, axis=1)

# 4. Find the best performing product index (add 1 for 1-based human indexing)
best_product = np.argmax(product_totals) + 1

# 5. Find the best performing month index (add 1 for 1-based human indexing)
best_month = np.argmax(monthly_totals) + 1

# Print Results
print("Total Sales")
print("----------------")
print(f"Product 1: {product_totals[0]}")
print(f"Product 2: {product_totals[1]}")
print(f"Product 3: {product_totals[2]}")
print(f"Product 4: {product_totals[3]}")
print()

print("Monthly Sales")
print("----------------")
print(f"Month 1: {monthly_totals[0]}")
print(f"Month 2: {monthly_totals[1]}")
print(f"Month 3: {monthly_totals[2]}")
print(f"Month 4: {monthly_totals[3]}")
print()

print("Average Sales Per Product")
print("----------------")
print(f"Product 1: {product_averages[0]:.2f}")
print(f"Product 2: {product_averages[1]:.2f}")
print(f"Product 3: {product_averages[2]:.2f}")
print(f"Product 4: {product_averages[3]:.2f}")
print()

print("Best Performing Product")
print("----------------")
print(f"Product {best_product}")
print()

print("Best Performing Month")
print("----------------")
print(f"Month {best_month}")