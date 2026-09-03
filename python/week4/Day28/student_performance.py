import numpy as np

# --- INITIALIZATION & SETUP ---
np.random.seed(42)

# Generate synthetic dataset
students = np.arange(101, 121)
subjects = np.array(["Python", "SQL", "Java", "Statistics", "Machine Learning"])
marks = np.random.randint(35, 101, size=(len(students), len(subjects)))

# Pre-calculate essential metrics
students_average = np.mean(marks, axis=1)
student_std = np.std(marks, axis=1)
subject_average = np.mean(marks, axis=0)

# --- SECTION 1: DATASET INFORMATION ---
print("--- DATASET INFORMATION ---")
print(f"Number of students : {len(students)}")
print(f"Number of subjects : {len(subjects)}")
print(f"Marks matrix shape : {marks.shape}")
print(f"Total marks counted: {marks.size}")

# --- SECTION 2: INDIVIDUAL PERFORMANCE METRICS ---
print("\n--- STUDENT AVERAGES ---")
for student_id, avg in zip(students, students_average):
    print(f"Student {student_id} Average: {avg:.2f}")

print("\n--- SUBJECT AVERAGES ---")
for subject_name, avg in zip(subjects, subject_average):
    print(f"{subject_name:18}: {avg:.2f}")

# --- SECTION 3: TOP & BOTTOM BENCHMARKS ---
best_sub_idx = np.argmax(subject_average)
worst_sub_idx = np.argmin(subject_average)
best_stud_idx = np.argmax(students_average)
worst_stud_idx = np.argmin(students_average)

print(f"\nBest Subject       : {subjects[best_sub_idx]} ({subject_average[best_sub_idx]:.2f})")
print(f"Worst Subject      : {subjects[worst_sub_idx]} ({subject_average[worst_sub_idx]:.2f})")
print(f"Best Student ID    : {students[best_stud_idx]} ({students[best_stud_idx]:.2f})")
print(f"Worst Student ID   : {students[worst_stud_idx]} ({students[worst_stud_idx]:.2f})")

# --- SECTION 4: OVERALL STATISTICAL DISTRIBUTION ---
print("\n--- OVERALL STATISTICS ---")
print(f"Mean               : {np.mean(marks):.2f}")
print(f"Median             : {np.median(marks):.2f}")
print(f"Minimum Mark       : {np.min(marks)}")
print(f"Maximum Mark       : {np.max(marks)}")
print(f"Standard Deviation : {np.std(marks):.2f}")

# --- SECTION 5: PASS / FAIL DISTRIBUTION ---
passed_mask = students_average >= 60
total_passed = np.sum(passed_mask)
total_failed = np.sum(~passed_mask)
pass_percentage = (total_passed / len(students)) * 100

print("\n--- PASS/FAIL ANALYSIS ---")
print(f"Passed Students    : {total_passed}")
print(f"Failed Students    : {total_failed}")
print(f"Pass Percentage    : {pass_percentage:.2f}%")

# --- SECTION 6: STANDING CATEGORIES ---
print("\n--- PERFORMANCE CATEGORIES ---")
# Vectorized assignment of category boundaries
categories = np.where(students_average >= 80, "Excellent",
             np.where(students_average >= 70, "Very Good",
             np.where(students_average >= 60, "Good", "Needs Improvement")))

for student_id, avg, cat in zip(students, students_average, categories):
    print(f"Student {student_id} | Average: {avg:.2f} | {cat}")

# --- SECTION 7: LEADERBOARD ---
print("\n--- TOP 5 STUDENTS ---")
rankings = np.argsort(students_average)[::-1]
for i, idx in enumerate(rankings[:5], start=1):
    print(f"{i}. Student {students[idx]} - {students_average[idx]:.2f}")

# --- SECTION 8: RECORD BREAKING METRICS ---
max_mark = np.max(marks)
stud_idx, sub_idx = np.unravel_index(np.argmax(marks), marks.shape)

print("\n--- HIGHEST INDIVIDUAL MARK ---")
print(f"Mark    : {max_mark}")
print(f"Student : {students[stud_idx]}")
print(f"Subject : {subjects[sub_idx]}")

# --- SECTION 9: SECONDARY COMPLEX ANALYSIS ---
print("\n--- SECONDARY DATASET ANALYSIS ---")

# 1 & 2. Consistency evaluations
most_consistent_idx = np.argmin(student_std)
most_inconsistent_idx = np.argmax(student_std)

print(f"1. Most Consistent Student   : ID {students[most_consistent_idx]} (Std Dev: {student_std[most_consistent_idx]:.2f})")
print(f"2. Most Inconsistent Student : ID {students[most_inconsistent_idx]} (Std Dev: {student_std[most_inconsistent_idx]:.2f})")

# 3. Peak metrics by axis
max_marks_per_subject = np.max(marks, axis=0)
best_sub_max_idx = np.argmax(max_marks_per_subject)
print(f"3. Subject with Highest Max  : {subjects[best_sub_max_idx]} (Max Mark: {max_marks_per_subject[best_sub_max_idx]})")

# 4. Target distribution tracking
students_above_80 = np.sum(students_average >= 80)
print(f"4. Students Scoring 80+ Avg  : {students_above_80} count")

# 5. Targeted slice mask output
below_60_mask = students_average < 60
print("5. Students with Average Below 60:")
for student_id, avg in zip(students[below_60_mask], students_average[below_60_mask]):
    print(f"   * Student {student_id} - Average: {avg:.2f}")
