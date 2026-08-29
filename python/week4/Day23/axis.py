import numpy as np

marks = np.array([
    [85, 90, 78],
    [72, 88, 91],
    [90, 95, 89],
    [65, 70, 68]
])

avg_stud = np.mean(marks, axis=1)
print(avg_stud)

avg_sub = np.mean(marks, axis=0)
print(avg_sub)

total_mark_stud = np.sum(marks, axis=1)
print(total_mark_stud)

total_mark_sub = np.sum(marks, axis=0)
print(total_mark_sub)

max_mark = np.max(marks)
print(max_mark)

min_mark = np.min(marks)
print(min_mark)

top_student_index = np.argmax(avg_stud)
print("Top Student Index:", top_student_index)