import numpy as np

employees = np.array([
    [101, 25, 45000],
    [102, 31, 65000],
    [103, 22, 38000],
    [104, 35, 85000],
    [105, 29, 55000],
    [106, 41, 95000],
    [107, 24, 42000],
    [108, 38, 72000]
])

# 1. Employees earning more than 60,000
employee_60k = employees[employees[:, 2] > 60000]

# 2. Employees younger than 30
employee_under_30 = employees[employees[:, 1] < 30]

# 3. Employees earning between 40,000 and 70,000
employee_earn_40kto70k = employees[(employees[:, 2] >= 40000) & (employees[:, 2] <= 70000)]

# 4. Highest salary
max_salary = np.max(employees[:, 2])

# 5. Employee ID of highest-paid employee
highest_paid_id = employees[np.argmax(employees[:, 2]), 0]

# 6. Average salary
avg_salary = np.mean(employees[:, 2])

# 7. Employees earning above average salary
above_avg_employees = employees[employees[:, 2] > avg_salary]

# Output Results
print("1. Employees earn more than 60000:\n", employee_60k)
print("\n2. Employees younger than 30:\n", employee_under_30)
print("\n3. Employees earning 40k to 70k:\n", employee_earn_40kto70k)
print("\n4. Highest Salary:", max_salary)
print("\n5. Employee ID of highest-paid employee:", highest_paid_id)
print("\n6. Average salary:", avg_salary)
print("\n7. Employees earning above average salary:\n", above_avg_employees)