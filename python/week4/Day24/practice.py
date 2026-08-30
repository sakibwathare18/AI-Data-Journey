import numpy as np

arr = np.arange(1, 21)

op1 = arr[[0,1,2,3,4]]

op2 = arr[[-5, -4, -3, -2, -1]]

op3 = arr[::2]

op4 = arr[::-1]

op5 = arr[5:14]

print(op1)
print(op2)
print(op3)
print(op4)
print(op5)

print("Conditional Replacement") 

marks = np.array([
    45, 67, 32, 89, 55,
    91, 28, 76, 49, 95
])

marks[marks < 40] = 40

print(marks)

print("np.where()")

marks = np.array([
    45, 67, 32, 89, 55,
    91, 28, 76, 49, 95
])

filter = np.where(marks>=60, "Pass", "Fail")

print(filter)