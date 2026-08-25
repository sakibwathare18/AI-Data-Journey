import numpy as np

#from list
arr1 = np.array([10,20,30])

#from tuple
arr2 = np.array((1,2,3,4,5))

#2D Array
arr3 = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr1)
print(arr1.shape)
print(arr2)
print(arr3)
print(arr3.shape) #shape - dimension sizes

print(arr3.ndim)  #ndim - number of dimension

print(arr3.size) #size - total number of elements

print(arr2.dtype)
print(arr3.dtype)

arr4 = np.array([2,4,6,8], dtype=float)
print(arr4.dtype)