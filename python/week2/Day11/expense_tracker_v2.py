file_path = r"\\wsl.localhost\Ubuntu\home\sakib\AI-Data-Journey\python\week2\Day11\expenses.txt"

with open(file_path,"r") as file :
    for line in file :
        print(line.strip())