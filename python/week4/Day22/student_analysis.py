import numpy as np

marks = np.array([
    85, 72, 91, 68, 77,
    95, 88, 64, 82, 90
])

add = marks + 5
print(add)

double = marks * 2
print(double)

percentage = (marks * 100) / 100
print(percentage)

highest = np.max(marks)
print(highest)

lowest = np.min(marks)
print(lowest)

avg = np.mean(marks)
print(avg)