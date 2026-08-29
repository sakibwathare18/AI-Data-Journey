import numpy as np

sales = np.array([
    1000, 1500, 1200, 1800,
    900, 2100, 1750
])

total_sales = np.sum(sales)
avg_sales = np.mean(sales)
min_sales = np.min(sales)
max_sales = np.max(sales)
id_max_sales = np.argmax(sales)

print("Total Sales:",total_sales)
print("Average Sales:",avg_sales)
print("Minimum Sales:",min_sales)
print("Maximum Sales:",max_sales)
print("Index of Max Sales:",id_max_sales)