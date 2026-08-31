import nnumpy as np

print("Transpose")
print("-----------------")

data = np.array([
    [10,20,30],
    [40,50,60]
])

print("Original:\n",data)
print("Shape:\n",data.shape)
transpose = data.T
print("Transpose:\n",transpose)
print("Transpose Shape:\n",transpose.shape)