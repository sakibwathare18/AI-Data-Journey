number = int(input("Enter Number :"))

square = lambda x: x * x
print(square(number))

cube = lambda x: x*x*x
print(cube(number))

a = 10
b = 20

even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(even_odd(number))

add = lambda a, b: a+b
print(add(a,b))

