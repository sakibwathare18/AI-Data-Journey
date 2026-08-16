def my_decorator(function):

    def wrapper():
        print("Starting function")

        function()

        print("Function finished")

    return wrapper

@my_decorator
def greet():
    print("Hello Sakib")

greet()


def my_decorator(func):

    def wrapper(*args,**kwargs):
        print("Starting function")
        result = func(*args,**kwargs)
        print("Function finished")
        return result
    return wrapper

@my_decorator
def add(a,b):
    return a+b

print(add(10,20))