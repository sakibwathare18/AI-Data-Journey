import numpy as np

data = np.array([
    12, 15, 18, 20, 22,
    25, 30, 35, 40, 45
])

print("Sum:",np.sum(data))
print("Mean:",np.mean(data))
print("Median:",np.median(data))
print("Minimum:",np.min(data))
print("Maximum:",np.max(data))
range = np.max(data) - np.min(data)
print("Range:",range)
print("Standard Deviation:",np.std(data))
print("Variance:",np.var(data))
print("25th Percentile:",np.percentile(data, 25))
print("75th Percentile:",np.percentile(data, 75))