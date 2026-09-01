import numpy as np

np.random.seed(42)

marks = np.random.randint(
    35,
    101,
    size=(20, 5)
)

# 1. Dimensions
num_students, num_subjects = marks.shape

# 2. Student & Subject Averages (Using axis)
student_averages = np.mean(marks, axis=1)
subject_averages = np.mean(marks, axis=0)

# 3. Overall Statistics
overall_mean = np.mean(marks)
overall_median = np.median(marks)
overall_min = np.min(marks)
overall_max = np.max(marks)
overall_std = np.std(marks)

# 4. Top Student (Using argmax)
top_student_idx = np.argmax(student_averages)
top_student_avg = student_averages[top_student_idx]

# 5. Passing Students (Using Boolean Masking)
passing_mask = student_averages >= 60
num_passing = np.sum(passing_mask)

print("====================================")
print("       STUDENT STATISTICS")
print("====================================")
print(f"Number of Students: {num_students}")
print(f"Number of Subjects: {num_subjects}")

print("\n------------------------------------")
print("STUDENT AVERAGES")
print("------------------------------------")
for i, avg in enumerate(student_averages):
    print(f"Student {i+1}: {avg:.2f}")

print("\n------------------------------------")
print("SUBJECT AVERAGES")
print("------------------------------------")
for i, avg in enumerate(subject_averages):
    print(f"Subject {i+1}: {avg:.2f}")

print("\n------------------------------------")
print("OVERALL STATISTICS")
print("------------------------------------")
print(f"Mean: {overall_mean:.2f}")
print(f"Median: {overall_median:.1f}")
print(f"Minimum: {overall_min}")
print(f"Maximum: {overall_max}")
print(f"Standard Deviation: {overall_std:.2f}")

print("\n------------------------------------")
print("TOP STUDENT")
print("------------------------------------")
print(f"Student: {top_student_idx + 1}")
print(f"Average: {top_student_avg:.2f}")

print("\n------------------------------------")
print("PASSING STUDENTS")
print("------------------------------------")
print(f"Number of students: {num_passing}")