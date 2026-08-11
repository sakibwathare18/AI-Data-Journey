from student import Student
from student_manager import StudentManager


manager = StudentManager()


while True:

    print("\n==============================")
    print("     STUDENT MANAGEMENT")
    print("==============================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Statistics")
    print("6. Save Student In File")
    print("7. Load Student From File")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        name = input("Enter name: ")

        try:

            age = int(input("Enter age: "))

            marks_input = input(
                "Enter marks separated by spaces: "
            )

            marks = [
                float(mark)
                for mark in marks_input.split()
            ]

            student = Student(
                name,
                age,
                marks
            )

            manager.add_student(student)

        except ValueError:

            print("Please enter valid numeric values.")

    elif choice == "2":

        manager.display_students()

    elif choice == "3":

        name = input("Enter student name: ")

        manager.search_student(name)

    elif choice == "4":

        name = input("Enter student name: ")

        manager.delete_student(name)

    elif choice == "5":

        manager.statistics()

    elif choice == "6":
    
            manager.save_students()

    elif choice == "7":
        
                manager.load_students()

    elif choice == "8":

        print("Goodbye!")

        break

    else:

        print("Invalid choice.")