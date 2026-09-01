import numpy as np

data = np.array([
    23, 45, 12, 67, 89,
    34, 90, 56, 78, 11
])

print("Minimum Value:",np.min(data))
print("Maximum Value:",np.max(data))

print("Minimum Position:",np.argmin(data))
print("Maximum Position:",np.argmax(data))