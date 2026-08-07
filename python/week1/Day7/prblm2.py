def even_odd(x):

    if x == 0 :
        return "Number is Zero..."
    elif x % 2 == 0 :
        return "Even Number"
    else :
        return "Odd Number"

number = int(input("Enter Number :"))

print(f"{number} is {even_odd(number)}")