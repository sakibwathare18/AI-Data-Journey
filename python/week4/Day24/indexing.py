import numpy as np

arr = np.array([
    10, 20, 30, 40, 50,
    60, 70, 80, 90, 100
])

fancy_index = arr[[0, 2, 5, 9]]

print(fancy_index)

data = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

first_row = data[0]
last_row = data[-1]
second_column = data[:,1]
last_column = data[:,-1]
top_left = data[:2,:2]
bottom_right = data[2:,2:]

print(first_row)
print(last_row)
print(second_column)
print(last_column)
print(top_left)
print(bottom_right)