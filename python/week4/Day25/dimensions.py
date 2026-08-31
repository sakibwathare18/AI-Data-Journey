import numpy as np

print("Flatten")
print("-----------------")

arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

flat = arr.flatten()
print(flat)

ravel = arr.ravel()
print(ravel)