tasks = []

while True:

    print("\n1.Add Task\n2.Remove Task\n3.View Tasks\n4.Exit")
    choice = int(input("Enter Choice :"))

    if choice == 1:
        task = input("Enter Task :")
        tasks.append(task)
        print("Task Added")

    elif choice == 2:
        task = input("Enter Task to Remove :")
        if task in tasks:
            tasks.remove(task)
            print("Task Removed")
        else:
            print("Task Not Found")
    elif choice == 3:
        print("Tasks :")
        print(tasks)

    elif choice == 4:
        print("Bye....")
        break
    else :
        print("Invalid Output")