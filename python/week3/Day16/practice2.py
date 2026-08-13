prices = [100, 250, 500, 750, 1000]

discount = list(
    map(lambda x: x-(x*10/100), prices)
)
print(discount)

greater_disc = list(
    filter(lambda x: x > 400, discount)
)
print(greater_disc)