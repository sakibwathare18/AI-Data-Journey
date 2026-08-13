from functools import reduce
numbers = [
    10, 15, 20, 25, 30,
    35, 40, 45, 50
]

even_num = list(
    filter(lambda x: x % 2 == 0, numbers)
)
print(even_num)

square = list(
    map(lambda x: x * x,numbers)
)
print(square)

total = reduce(lambda a,b: a+b, numbers)
print(total)