import numpy as np


# -----------------------------
# DATA GENERATION
# -----------------------------

np.random.seed(42)

students = np.arange(101, 121)

subjects = np.array([
    "Python",
    "SQL",
    "Java",
    "Data Science"
])

marks = np.random.randint(
    35,
    101,
    size=(20, 4)
)


# -----------------------------
# BASIC INFORMATION
# -----------------------------

print("=" * 50)
print("       STUDENT DATA ANALYSIS")
print("=" * 50)

print("Number of Students:", marks.shape[0])
print("Number of Subjects:", marks.shape[1])

print("\nSubjects:")
print(subjects)


# -----------------------------
# STUDENT ANALYSIS
# -----------------------------

student_average = np.mean(
    marks,
    axis=1
)

student_std = np.std(
    marks,
    axis=1
)

best_student_index = np.argmax(
    student_average
)

worst_student_index = np.argmin(
    student_average
)

print("\n" + "-" * 50)
print("STUDENT ANALYSIS")
print("-" * 50)

print(
    "Best Student:",
    students[best_student_index]
)

print(
    "Best Average:",
    student_average[best_student_index]
)

print(
    "Lowest Student:",
    students[worst_student_index]
)

print(
    "Lowest Average:",
    student_average[worst_student_index]
)


# -----------------------------
# SUBJECT ANALYSIS
# -----------------------------

subject_average = np.mean(
    marks,
    axis=0
)

subject_max = np.max(
    marks,
    axis=0
)

subject_min = np.min(
    marks,
    axis=0
)

print("\n" + "-" * 50)
print("SUBJECT ANALYSIS")
print("-" * 50)

for i in range(len(subjects)):
    print(
        subjects[i],
        "Average:",
        round(subject_average[i], 2),
        "Min:",
        subject_min[i],
        "Max:",
        subject_max[i]
    )


# -----------------------------
# OVERALL STATISTICS
# -----------------------------

print("\n" + "-" * 50)
print("OVERALL STATISTICS")
print("-" * 50)

print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))
print("Std Dev:", np.std(marks))


# -----------------------------
# PASSING ANALYSIS
# -----------------------------

PASS_MARK = 60

passed = student_average >= PASS_MARK

passing_students = students[passed]

print("\n" + "-" * 50)
print("PASSING ANALYSIS")
print("-" * 50)

print(
    "Passing Students:",
    passing_students
)

print(
    "Number Passed:",
    np.sum(passed)
)

passing_percentage = (
    np.sum(passed) /
    len(students)
) * 100

print(
    "Passing Percentage:",
    round(passing_percentage, 2),
    "%"
)


# -----------------------------
# TOP 5
# -----------------------------

ranking = np.argsort(
    student_average
)[::-1]

top5 = ranking[:5]

print("\n" + "-" * 50)
print("TOP 5 STUDENTS")
print("-" * 50)

for position in top5:
    print(
        "Student:",
        students[position],
        "| Average:",
        round(student_average[position], 2)
    )