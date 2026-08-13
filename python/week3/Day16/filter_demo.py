numbers = [
    12, 5, 18, 3, 25, 30, 7
]

even = list(
    filter(lambda x: x % 2 == 0, numbers)
)
print(even)

greater_10 = list(
    filter(lambda x: x > 10, numbers)
)
print(greater_10)

between = list(
    filter(lambda x: x > 5 and x < 20, numbers)
)
print(between)