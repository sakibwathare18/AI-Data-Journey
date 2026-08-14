# def even_number(limit):
#     for number in range(2, limit +1, 2):
#         yield number

# for number in even_number(10):
#     print(number)

# def square(limit):
#     for number in range(1, limit +1):
#             yield number*number

# for number in square(5):
#     print(number)

# def countdown(number):
#     while number > 0 :
#         yield number
#         number -= 1

# for n in countdown(5):
#     print(n)

def generate_number():
    for i in range(1, 100001):
        yield i

total = 0
for number in generate_number():
    total += number
print(total)