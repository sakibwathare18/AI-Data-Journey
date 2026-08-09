file_path = r"\\wsl.localhost\Ubuntu\home\sakib\AI-Data-Journey\python\week2\Day11\expenses.txt"
total = 0

with open(file_path,"r") as file :
    for line in file :
        category, amount = line.strip().split(",")

        total += float(amount)

print("Total Expenses :",total)