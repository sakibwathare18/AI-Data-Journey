import numpy as np

marks = np.array([
    45, 67, 82, 91, 55,
    73, 88, 39, 95, 61
])

marks_a = marks[marks > 80]
marks_b = marks[marks < 50]
marks_c = marks[(marks > 60) & (marks < 90)]
marks_d = marks[marks == 95]

print("Marks above 80 :",marks_a)
print("Marks below 50 :",marks_b)
print("Marks between 60 and 90 :",marks_c)
print("Marks equal to 95 :",marks_d)