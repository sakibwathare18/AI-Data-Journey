# import re


# students = [
#     ("Sakib", 85),
#     ("Rahul", 72),
#     ("Amit", 91),
#     ("Neha", 89)
# ]

# sorted_stud = sorted(students, key=lambda x :x[1], reverse=True)

# for name, marks in sorted_stud:
#     print(f"{name} {marks}")


# def even_numbers(numbers):
#     for number in numbers:
#         if number % 2 == 0:
#             yield number

# number = range(1,21)

# for number in even_numbers(number):
#     print(number)


# def extract_order_ids(text):
#     yield re.findall(r'Order (\d{5})',text)

# text = """
# Order 12345
# Order 67890
# Invalid order
# Order 45678
# Order ABCDE
# Order 98765
# """

# order_ids = extract_order_ids(text)

# for order_id in order_ids:
#     print(order_id)


# def log_function(func):
#     def wrapper(*args,**kwargs):
#         print(f"Running: {func.__name__}")
#         return func(*args,**kwargs)
#     return wrapper

# @log_function
# def clean_data(data):
#     print(f"Data Cleaned: {data}")

# clean_data("raw_user_info")



# def statistics(*numbers):
#     total_val = sum(numbers)
#     min_val = min(numbers)
#     max_val = max(numbers)
#     avg_val = total_val/len(numbers) if numbers else 0

#     return {
#         "Total": total_val,
#         "Minimum": min_val,
#         "Maximum": max_val,
#         "Average": avg_val
#     }

# result = statistics(10,20,30,40,50)
# print(result)


def create_config(**kwargs):
    return kwargs

config = create_config(
    source="customers.csv",
    delimeter=",",
    encoding="utf-8",
    clean=True,
    output="customers_clean.csv"
)
for key, value in config.items():
    print(f"{key}: {value}")