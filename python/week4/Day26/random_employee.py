import numpy as np

np.random.seed(42)

salaries = np.random.randint(
    20000,
    100000,
    size=50
)

avg_salary = np.mean(salaries)
median_salary = np.median(salaries)
min_salary = np.min(salaries)
max_salary = np.max(salaries)
std_salary = np.std(salaries)

abv_avg = salaries[salaries > avg_salary]

print("Employee")
print("================")

print("\nAverage Salary:",avg_salary)
print("\nMedian Salary:",median_salary)
print("\nMinimum Salary:",min_salary)
print("\nMaximum Salary:",max_salary)
print("\nStandard Deviation:",std_salary)

print("Employees above avg:",abv_avg)