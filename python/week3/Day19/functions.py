def square(x):
    return x*x

def cube(x):
    return x*x*x

def execute(function, value):
    return function(value)

print(execute(square, 5))
print(execute(cube,3))