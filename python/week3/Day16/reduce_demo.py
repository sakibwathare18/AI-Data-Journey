from functools import reduce

numbers = [5, 10, 15, 20]

total = reduce(lambda a, b: a+b, numbers)
print(total)

product = reduce(lambda a, b: a*b, numbers)
print(product)