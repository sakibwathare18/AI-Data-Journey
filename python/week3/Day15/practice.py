students = [
    {"name": "Sakib", "marks": 85},
    {"name": "Rahul", "marks": 42},
    {"name": "Amit", "marks": 91},
    {"name": "Priya", "marks": 35},
    {"name": "Neha", "marks": 78}
]
updated_name = [
    student["name"] for student in students
    if student["marks"] >= 75
]
print(updated_name)