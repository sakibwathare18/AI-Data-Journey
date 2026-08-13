students = [
    {"name": "Sakib", "marks": 85},
    {"name": "Rahul", "marks": 42},
    {"name": "Amit", "marks": 91},
    {"name": "Priya", "marks": 35},
    {"name": "Neha", "marks": 78}
]

marks_75 = list(
    filter(lambda x: x["marks"] >= 75,students)
)
print(marks_75)

s_names = list(
    map(lambda x: x["name"],marks_75)
)
print(s_names)