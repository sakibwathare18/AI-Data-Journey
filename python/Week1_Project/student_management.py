def cal_marks(marks):
    return sum(marks)

def cal_avg(marks):
    count = len(marks)
    total_marks = sum(marks)
    return total_marks / count

def cal_grade(marks):
    total_marks = sum(marks)

    if total_marks >= 90 :
        return "A"
    elif total_marks >= 70 :
        return "B"
    elif total_marks >= 60 :
        return "C"
    elif total_marks >= 40 :
        return "D"
    else :
        return "F"

while True:
    name = input("Enter Student Name :")
    marks = [
        int(input("Enter 1st Marks :")),
        int(input("Enter 2nd Marks :")),
        int(input("Enter 3rd Marks :"))
    ]

    print("Stuent Name :",name)
    print("Total Marks :",cal_marks(marks))
    print("Average Marks :",cal_avg(marks))
    print("Grade :",cal_grade(marks))
    repeat = input("\nDo you want to enter another student? (yes/no): ").strip().lower()

    if repeat not in ['yes','y']:
        print("Exiting the Program...")
        break

