import numpy as np

print("Reshape")
print("-----------------")

arr = np.arange(1, 13)

arr1 = arr.reshape(2,6)
arr2 = arr.reshape(3,4)
arr3 = arr.reshape(4,3)
arr4 = arr.reshape(6,2)

print(arr1)
print(arr2)
print(arr3)
print(arr4)

print("Automatic Dimension")
print("-----------------")

arr = np.arange(1,25)

arr1 = arr.reshape(4, -1)
arr2 = arr.reshape(6, -1)
arr3 = arr.reshape(8, -1)

print(arr1)
print(arr2)
print(arr3)
