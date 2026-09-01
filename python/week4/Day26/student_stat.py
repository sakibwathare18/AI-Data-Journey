import numpy as np

marks = np.array([
    [85, 90, 78, 92],
    [72, 88, 91, 80],
    [90, 95, 89, 94],
    [65, 70, 68, 72],
    [95, 92, 96, 98]
])

student_avg = np.mean(marks, axis=1)
subject_avg = np.mean(marks, axis=0)

std_student = np.std(marks, axis=1)
std_subject = np.std(marks, axis=0)

highest_mark = np.max(marks)
lowest_mark = np.min(marks)

print("Average per student:",student_avg)
print("Average per subject:",subject_avg)

print("Standard deviation per student:",std_student)
print("Standard deviation per subject:",std_subject)

print("Highest overall mark:",highest_mark)
print("Lowest overall mark:",lowest_mark)
