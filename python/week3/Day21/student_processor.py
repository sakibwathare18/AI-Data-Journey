import re
from functools import wraps

records = [
    "Sakib,21,sakib@gmail.com,9876543210,85",
    "Rahul,22,rahul@gmail.com,9123456780,72",
    "Amit,17,amit@gmail.com,9988776655,91",
    "Neha,23,neha@gmail.com,9876501234,88",
    "Priya,25,invalid-email,9876501111,95",
    "Invalid Data",
    "Rohan,20,rohan@gmail.com,12345,67",
    "Anita,19,anita@gmail.com,9876543211,78"
]

def log_function(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Running: {function.__name__}")
        result = function(*args, **kwargs)
        print(f"Finished: {function.__name__}\n")
        return result
    return wrapper

@log_function
def parse_record(record):
    parts = record.split(",")
    if len(parts) != 5:
        return None
    try:
        return {
            "name": parts[0].strip(),
            "age": int(parts[1].strip()),
            "email": parts[2].strip(),
            "phone": parts[3].strip(),
            "marks": int(parts[4].strip())
        }
    except ValueError:
        return None

def valid_email(email):
    pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
    return re.match(pattern, email) is not None

def valid_phone(phone):
    pattern = r"^\d{10}$"
    return re.match(pattern, phone) is not None

def calculate_grade(marks):
    if marks >= 90: return "A"
    elif marks >= 80: return "B"
    elif marks >= 70: return "C"
    elif marks >= 60: return "D"
    else: return "F"

@log_function
def validate_student(student):
    if student["age"] < 18:
        return False
    if student["marks"] < 0 or student["marks"] > 100:
        return False
    if not valid_email(student["email"]):
        return False
    if not valid_phone(student["phone"]):
        return False
    return True

def process_records(records):
    """Processes records one by one, streaming valid students on demand."""
    for record in records:
        student_dict = parse_record(record)
        if student_dict and validate_student(student_dict):
            student_dict["name"] = student_dict["name"].strip().title()
            student_dict["grade"] = calculate_grade(student_dict["marks"])
            yield student_dict

def top_students(students, minimum_marks=80):
    return [
        student
        for student in students
        if student["marks"] >= minimum_marks
    ]

def statistics(*students):
    if not students:
        return {"total": 0, "average": 0.0, "highest": None, "lowest": None}
    
    marks_list = [student["marks"] for student in students]
    total_count = len(marks_list)
    
    return {
        "total": total_count,
        "average": round(sum(marks_list) / total_count, 2),
        "highest": max(marks_list),
        "lowest": min(marks_list)
    }

# --- Execution & Dashboard Output Formatting ---

if __name__ == "__main__":
    print("========================================")
    print("       STUDENT DATA PROCESSOR")
    print("========================================\n")

    # Consume the generator stream into a list to compute analytics
    valid_students_list = list(process_records(records))
    
    print("Valid Students:")
    print("----------------------------------------")
    for student in valid_students_list:
        print(f"{student['name']:<6} | {student['age']} | {student['marks']} | {student['grade']}")

    print("\n========================================")
    print("STATISTICS")
    print("========================================\n")
    
    stats = statistics(*valid_students_list)
    print(f"Total Students : {stats['total']}")
    print(f"Average Marks  : {stats['average']}")
    print(f"Highest Marks  : {stats['highest']}")
    print(f"Lowest Marks   : {stats['lowest']}")

    print("\n========================================")
    print("TOP STUDENTS")
    print("========================================\n")
    
    elites = top_students(valid_students_list, minimum_marks=80)
    for student in elites:
        print(f"{student['name']:<6} | {student['marks']}")
