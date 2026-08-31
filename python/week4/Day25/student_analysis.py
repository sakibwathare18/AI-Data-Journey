import numpy as np

marks = np.array([
    [85, 90, 78],
    [72, 88, 91],
    [90, 95, 89],
    [65, 70, 68],
    [95, 92, 96]
])

student_avg = np.mean(marks, axis=1)
subject_avg = np.mean(marks, axis=0)
student_total = np.sum(marks, axis=1)
subject_total = np.sum(marks, axis=0)

print("Student Average:\n",student_avg)
print("Subject Average:\n",subject_avg)
print("Student Total:\n",student_total)
print("Subject Total:\n",subject_total)

tarnspose_marks = marks.T

print("Shape before transpose:\n",marks.shape)
print("Shape after transpose:\n",tarnspose_marks.shape)