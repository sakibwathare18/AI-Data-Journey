import numpy as np

marks = np.array([
    [85, 90, 78, 92],
    [72, 88, 91, 80],
    [90, 95, 89, 94],
    [65, 70, 68, 72],
    [95, 92, 96, 98]
])

shape = marks.shape

stud_size = marks.shape[0]
sub_size = marks.shape[1]

avg_stud = marks.mean(axis=1)
avg_sub = marks.mean(axis=0)

total_stud = marks.sum(axis=1)
total_sub = marks.sum(axis=0)

highest_mark = np.max(total_stud)
lowest_mark = np.min(total_stud)

top_stud = np.argmax(total_stud) + 1

tranpose_marks = marks.T

print("========================")
print("STUDENT REPORT")
print("========================\n")
print("Dataset Shape:\n",shape)

print("\nNumber of Students:\n",stud_size)

print("\nNumber of Subjects:\n",sub_size)

print("\nStudent Averages:\n",np.round(avg_stud, 2))

print("\nSubject Averages:\n",np.round(avg_sub, 2))

print("\nStudent Totals:\n",total_stud)

print("\nSubject Totals:\n",total_sub)

print("\nHighest Overall Mark:\n",highest_mark)

print("\nLowest Overall Mark:\n",lowest_mark)

print("\nTop Student:\n",top_stud)

print("\nTransposed Shape:\n",tranpose_marks.shape)