def calculate_grade(marks):

    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else :
        return "F"

name = input("Enter Student Name :")
marks = int(input("Enter Students Marks :"))

grade = calculate_grade(marks)

print(f"{name} marks is {marks} and grade is {grade}")
