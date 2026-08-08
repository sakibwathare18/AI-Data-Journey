students = []

while True:

    print("\n1.Add Student\n2.Dipslay Students\n3.Search Student\n4.Exit")

    choice = input("Enter Choice :")

    if choice == "1" :
        name = input("Enter Name :")
        marks = int(input("Enter Marks :"))

        student = {
            "Name": name,
            "Marks": marks
        }

        students.append(student)

        print("Student Added Successfully!")

    elif choice == "2" :
        for student in students:
            print(
                "Name:",student["Name"],
                "| Marks:",student["Marks"]
            )
    elif choice == "3" :
        name = input("Enter name to Search :")
        found = False

        for student in students:

            if student["Name"].lower() == name.lower():
                print("Student found!")
                print("Marks:", student["Marks"])
                found = True
        if not found:
            print("Student Not Found")
    elif choice == "4":
        print("Bye..")
        break
    else :
        print("Invalid Output")