numbers = [2, 4, 6, 8, 10]

double = list(
    map(lambda x: x * 2, numbers)
)
print(double)

square = list(
    map(lambda x: x * x, numbers)
)
print(square)

to_string = list(
    map(lambda x: str(x), numbers)
)
print(to_string)