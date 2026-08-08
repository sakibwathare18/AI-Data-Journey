stud_name = []
stud_marks = []

def add_stud():
    name = input("Enter Name of Student :")

    marks = int(input("Enter Marks :"))

    stud_name.append(name)
    stud_marks.append(marks)

def disp_stud():
    for i in range(len(stud_name)):
        print(f"{i + 1}. Name: {stud_name[i]} | Marks: {stud_name[i]}")

def search_stud():
    student = input("\nEnter Student to Search :")
    if student in stud_name:
        id = stud_name.index(student)
        print(f"Name: {stud_name[id]} | Marks: {stud_name[id]}")
    else :
        print("Student not found")

def update_marks():
    student = input("Enter Student to Update Marks :")
    if student in stud_name:
        id = stud_name.index(student)
        marks = int(input("Enter New Marks :"))
        stud_marks[id] = marks
        print(f"Name: {stud_name[id]} | Marks: {stud_name[id]}")
        print("Marks Updated")
    else :
        print("Student not found")

def delete_stud():
    if not stud_marks:
        print("Students Not Found")

    name = input("Enter Student to Delete :")
    if name in stud_name:
        id = stud_name.index(name)
        stud_name.pop(id)
        stud_marks.pop(id)
        print("Student Deleted")
    else:
        print("Student not found")

while True :
    print("\n1.Add Student\n2.Display Student\n3.Search Student\n4.Update Marks\n5.Delete Student\n6.Exit")
    choice = int(input("Enter Choice :\n"))

    if choice == 1 :
        add_stud()
    elif choice == 2 :
        disp_stud()
    elif choice == 3 :
        search_stud()
    elif choice == 4 :
        update_marks()
    elif choice == 5 :
        delete_stud()
    elif choice == 6 :
        print("Bye..")
        break
    else:
        print("Invalid Choice")
