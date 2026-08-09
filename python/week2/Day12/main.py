import calculator as calc
import password_generator as pas
import datetime_demo as dt

while True:
    print("\n1. Calculator\n2. Generate Password\n3. Show Date & Time\n4. Exit")
    choice = int(input("Enter Choice :"))

    if choice == 1 :
        x = int(input("Enter First Number :"))
        y = int(input("Enter Second Number :"))
        print(calc.add(x,y))
        print(calc.substract(x,y))
        print(calc.multiply(x,y))
        print(calc.divide(x,y))

    elif choice == 2 :
        pas.password_gen()
    elif choice == 3:
        dt.dt()
    elif choice == 4 :
        print("Bye..")
        break
    else :
        print("Invalid Choice.")