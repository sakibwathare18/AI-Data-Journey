names = [
    "sakib",
    "RAHUL",
    "Amit",
    "neha",
    "PRIYA"
]

name = [i.strip().lower() for i in names]

print("\n".join(name))

ages = [21,17,25,14,32,16,28]

adults = [age for age in ages if age >= 18]
print(adults)

adults = list(filter(lambda age: age >= 18, ages))
print(adults)

numbers = [1,2,3,4,5]

square = list(map(lambda i: i**2,numbers))
print(square)

square = [i**2 for i in numbers]
print(square)