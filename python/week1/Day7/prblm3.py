
def fact(x):
    factorial = 1
    for i in range(1,x+1):
        factorial *= i

    return factorial

number = int(input("Enter Number :"))

print(fact(number))