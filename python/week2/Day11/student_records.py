file_path = r"\\wsl.localhost\Ubuntu\home\sakib\AI-Data-Journey\python\week2\Day11\stud_records.txt"
def add_stud():
    with open(file_path,"a") as file :
        name = input("Enter Name of Student :")
        try:
            age = int(input("Enter Age :"))
            marks = int(input("Enter Marks :"))
        except ValueError:
            print("Enter Valid Number (Number Format).")
        file.write(f"{name},{age},{marks}")

def view_stud():
    with open(file_path,"r") as file:
        for line in file:
            print(line.strip())
while True:
    print("\n1. Add Student\n2. View Students\n3. Exit")
    choice = int(input("Enter Choice :"))

    if choice == 1 :
        add_stud()
    elif choice == 2 :
        view_stud()
    elif choice == 3:
        print("Bye...")
        break
    else :
        print("Invalid Choice.")

