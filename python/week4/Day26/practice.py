import numpy as np

marks = np.array([
    45, 67, 82, 91, 55,
    73, 88, 39, 95, 61
])

print("Total:", np.sum(marks))
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))
print("Standard Deviation:", np.std(marks))
print("Variance:", np.var(marks))