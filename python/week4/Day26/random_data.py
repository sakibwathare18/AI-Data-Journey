import numpy as np

print("Generate Data")
print("=====================")

np.random.seed(42)

marks = np.random.randint(
    0,
    101,
    size=100
)

print("Mean:",np.mean(marks))
print("Median:",np.median(marks))
print("Minimum:",np.min(marks))
print("Maximum:",np.max(marks))
print("Standard Deviation:",np.std(marks))