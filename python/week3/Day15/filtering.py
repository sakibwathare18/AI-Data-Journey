numbers = list(range(1, 51))

even_numbers = [
    i for i in numbers
    if i % 2 == 0
]
odd_numbers = [
    i for i in numbers
    if i % 2 != 0
]

print(even_numbers)
print(odd_numbers)