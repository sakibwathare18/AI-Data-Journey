file_path = r"\\wsl.localhost\Ubuntu\home\sakib\AI-Data-Journey\python\week2\Day11\expenses.txt"


while True:
    print("\n1. Add Expenses\n2. View Expenses\n3. Calculate Total\n4. Average Expenses\n5. Highest & Lowest Expense\n6. Category Expenses\n7. Exit")
    choice = int(input("Enter Choice :"))

    if choice == 1 :
        category = input("Enter Category :")
        try :
            amount = float(input("Enter Amount :"))
        except ValueError :
            print("Enter a Valid Amount.")

        with open(file_path,"a") as file :
            file.write(f"{category},{amount}\n")

            print("Expenses Added.")

    elif choice == 2 :
        with open(file_path,"r") as file :
            for line in file :
                print(line.strip())
    elif choice == 3 :
        total = 0

        with open(file_path,"r") as file :
            for line in file :
                category, amount = line.strip().split(",")

                total += float(amount)

        print("Total Expenses :",total)
    elif choice == 4 :
        total = 0
        count = 0
        
        with open(file_path,"r") as file :
            for line in file :
                category, amount = line.strip().split(",")
        
                total += float(amount)
                count += 1
                avg = total / count
        
        print("Average :",avg)
    elif choice == 5 :
        high_cat = None
        low_cat = None
        highest_amount = None 
        lowest_amount = None
        
        with open(file_path,"r") as file :
            for line in file :
                category, amount = line.strip().split(",")     
                amount = float(amount)
        
                if highest_amount is None or amount > highest_amount :
                    highest_amount = amount
                    high_cat = category
        
                if lowest_amount is None or amount < lowest_amount :
                    lowest_amount = amount
                    low_cat = category
        
        print(f"Highest Category is {high_cat} and amount is {highest_amount}")
        print(f"Lowest Category is {low_cat} and amount is {lowest_amount}")

    elif choice == 6 :
        search_category = input("Enter Category to Search :")
        cat_total = 0
        found = False

        with open(file_path,"r") as file:
            for line in file :
                category, amount = line.strip().split(",")     
                if category == search_category :
                    print(f"Category : {category} | Amount : {amount}")
                    cat_total += float(amount)
                    found = True
        if found:
            print(f"Total for {search_category}: {cat_total:.2f}")
        else :
            print("Category Not Found")
    elif choice == 7 :
        print("Byee")
        break
    else :
        print("invalid Choice")