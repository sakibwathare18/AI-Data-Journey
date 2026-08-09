category = input("Enter Category :")
amount = float(input("Enter Amount :"))

file_path = r"\\wsl.localhost\Ubuntu\home\sakib\AI-Data-Journey\python\week2\Day11\expenses.txt"
with open(file_path,"a") as file :
    file.write(f"{category},{amount}\n")

print("Expenses Saved.")