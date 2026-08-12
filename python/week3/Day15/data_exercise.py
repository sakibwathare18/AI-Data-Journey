temperatures = [
    25, 31, 28, 35, 22,
    30, 40, 27, 33, 29
]

above_30 = [
    temp for temp in temperatures
    if temp > 30
]

below_30 = [
    temp for temp in temperatures
    if temp < 30
]

fahrenheit = [
    temp * 9/5 + 32 for temp in temperatures
]

print(f"Above 30 Tempratures : {above_30}")
print(f"Below 30 Tempratures : {below_30}")
print(f"Celsiues to Fahrenheit : {fahrenheit}")