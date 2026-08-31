import numpy as np

sales = np.array([
    1000, 1200, 1100,
    1300, 1400, 1500,
    1600, 1550, 1700,
    1800, 1900, 2000
])

reshape_sales = sales.reshape(4,3)

total_per_quarter = reshape_sales.sum(axis=1)
avg_per_quarter = reshape_sales.mean(axis=1)
total_per_month =reshape_sales.sum(axis=0)
avg_per_month = reshape_sales.mean(axis=0)
best_quarter = np.argmax(total_per_quarter)+1


print("Total sales per quarter:\n",total_per_quarter)
print("Average sales per quarter:\n",avg_per_quarter)
print("Total sales per month:\n",total_per_month)
print("Average sales per month:\n",avg_per_month)
print("Best quarter:\n",best_quarter)