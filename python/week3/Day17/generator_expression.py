def number():
    for i in range(1, 101):
        yield i

def even_num(nums):
    for i in nums:
        if i % 2 == 0:
            yield i

def square_num(nums):
    for i in nums:
        yield i ** 2

square = square_num(even_num(number()))
for i in square:
    print(i)