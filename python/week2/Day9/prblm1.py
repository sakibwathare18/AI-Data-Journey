numbers = []

for i in range(1,11):
    x = int(input("Enter Number :"))
    numbers.append(x)

print("Max :",max(numbers))
print("Min :",min(numbers))
print("Avetage :",sum(numbers)/len(numbers))