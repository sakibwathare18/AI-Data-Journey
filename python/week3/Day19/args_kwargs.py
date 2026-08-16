# def calculate_sum(*args):
#     return sum(args)

# print(calculate_sum(10,20))
# print(calculate_sum(1,2,3,4,5))
# print(calculate_sum(100,200,300,400))

def student_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

student_details(
    name="Sakib",
    age=21,
    course="Data Science",
    city="Kolhapur"
)