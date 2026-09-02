import numpy as np

# -----------------------------
# DATA GENERATION
# -----------------------------

np.random.seed(100)

employees = np.arange(1001, 1021)

skills = np.array([
    "Python",
    "SQL",
    "Communication",
    "Problem Solving"
])

performance = np.random.randint(
    40,
    101,
    size=(20, 4)
)

# -----------------------------
# BASIC INFORMATION
# -----------------------------

print("=" * 50)
print("       EMPLOYEE DATA ANALYSIS")
print("=" * 50)

print("Number of Employees:", performance.shape[0])
print("Number of Skills:", performance.shape[1])
print("\nMatrix Shape:", performance.shape)

# -----------------------------
# EMPLOYEES ANALYSIS
# -----------------------------

emp_average = np.mean(
    performance,
    axis=1
)

high_emp = np.argmax(emp_average)
low_emp = np.argmin(emp_average)

print("=" * 50)
print("       EMPLOYEE ANALYSIS")
print("=" * 50)

for i in range(len(employees)):
    print(f"Employee {employees[i]}: {round(emp_average[i], 2)}")

print("-" * 50)
print("Highest performing employee:", employees[high_emp])
print("Lowest performing employee:", employees[low_emp])

# -----------------------------
# SKILL ANALYSIS
# -----------------------------

skill_average = np.mean(performance, axis=0)
skill_max = np.max(performance, axis=0)
skill_min = np.min(performance, axis=0)
skill_std = np.std(performance, axis=0)

best_skill_idx = np.argmax(skill_average)
weakest_skill_idx = np.argmin(skill_average)

print("\n" + "=" * 50)
print("       SKILL ANALYSIS")
print("=" * 50)

for i in range(len(skills)):
    print(f"\nSkill: {skills[i]}")
    print(f"  Average:            {round(skill_average[i], 2)}")
    print(f"  Maximum Score:      {skill_max[i]}")
    print(f"  Minimum Score:      {skill_min[i]}")
    print(f"  Standard Deviation: {round(skill_std[i], 2)}")

print("-" * 50)
print("Best overall skill (Highest Avg):  ", skills[best_skill_idx])
print("Weakest overall skill (Lowest Avg):", skills[weakest_skill_idx])

# -----------------------------
# OVERALL WORKFORCE PERFORMANCE
# -----------------------------

overall_mean = np.mean(performance)
overall_median = np.median(performance)
overall_min = np.min(performance)
overall_max = np.max(performance)
overall_std = np.std(performance)

print("\n" + "=" * 50)
print("       OVERALL WORKFORCE PERFORMANCE")
print("=" * 50)
print(f"Overall Mean Score:       {round(overall_mean, 2)}")
print(f"Overall Median Score:     {round(overall_median, 2)}")
print(f"Overall Minimum Score:    {overall_min}")
print(f"Overall Maximum Score:    {overall_max}")
print(f"Overall Std Deviation:    {round(overall_std, 2)}")
print("=" * 50)

# -----------------------------
# PERFORMANCE CATEGORIES
# -----------------------------

excellent_mask = (emp_average >= 85)
good_mask      = (emp_average >= 70) & (emp_average < 85)
average_mask   = (emp_average >= 60) & (emp_average < 70)
needs_work_mask = (emp_average < 60)

count_excellent  = np.sum(excellent_mask)
count_good       = np.sum(good_mask)
count_average    = np.sum(average_mask)
count_needs_work = np.sum(needs_work_mask)

print("\n" + "=" * 50)
print("       PERFORMANCE CATEGORIES TALLY")
print("=" * 50)
print(f"Excellent (>= 85):   {count_excellent} employee(s)")
print(f"Good (70 - 84.9):    {count_good} employee(s)")
print(f"Average (60 - 69.9): {count_average} employee(s)")
print(f"Needs Work (< 60):   {count_needs_work} employee(s)")
print("=" * 50)

# -----------------------------
# BONUS CHALLENGE: TOP 3 EMPLOYEES (NO LOOPS)
# -----------------------------

top_3_indices = np.argsort(emp_average)[-3:][::-1]

print("\n" + "=" * 50)
print("       TOP 3 PERFORMING EMPLOYEES")
print("=" * 50)

print(f"Rank 1: Employee {employees[top_3_indices[0]]} | Average Score: {round(emp_average[top_3_indices[0]], 2)}")
print(f"Rank 2: Employee {employees[top_3_indices[1]]} | Average Score: {round(emp_average[top_3_indices[1]], 2)}")
print(f"Rank 3: Employee {employees[top_3_indices[2]]} | Average Score: {round(emp_average[top_3_indices[2]], 2)}")

print("=" * 50)
