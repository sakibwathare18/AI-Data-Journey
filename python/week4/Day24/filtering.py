import numpy as np

marks = np.array([
    [85, 90, 78],
    [72, 88, 91],
    [90, 95, 89],
    [65, 70, 68],
    [95, 92, 96]
])

above_90 = marks[marks > 90]
math_90 = marks[marks[:,0] > 90]
avg_85 = marks[np.mean(marks, axis=1) > 85]
any_above_95_mask = (marks > 95).any(axis=1)
any_above_95 = marks[any_above_95_mask]  

print(above_90)
print(math_90)
print(avg_85)
print(any_above_95)