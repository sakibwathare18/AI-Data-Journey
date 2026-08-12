marks = [35, 67, 89, 42, 91, 28, 76]
passed = [
    mark for mark in marks
    if mark >= 40
]
failed = [
    mark for mark in marks
    if mark < 40
]
print(f"Passed Students : {passed}")
print(f"Failed Students : {failed}")

names = [
    "sakib",
    "rahul",
    "amit",
    "priya"
]
upper_names = [
    name.upper() for name in names
]
print(upper_names)