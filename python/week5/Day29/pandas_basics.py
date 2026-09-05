import pandas as pd

# marks = pd.Series([85, 72, 91, 64, 78])

# print(marks)

# marks = pd.Series(
#     [85, 72, 91],
#     index=["Rahul","Amit","Sneha"]
# )

# print(marks)
# print(marks["Rahul"])

data = {
    "Student": [101, 102, 103, 104],
    "Name": ["Amit", "Sneha", "Rahul", "Priya"],
    "Python": [85, 92, 76, 88],
    "SQL": [78, 89, 82, 91]
}

df = pd.DataFrame(data)

print(df)

print(df.shape)

print(df.columns)

print(df.columns.tolist())

print(df.dtypes)

print(df.head())

print(df.head(2))

print(df.tail())

print(df.tail(2))

print(df.info())

print(df.describe())

print(df["Python"])

print(df.iloc[0])

print(df.iloc[0:2])

print(df.iloc[1, 2])

print(df.loc[0, "Python"])

#Filtering Data

print(df[df["Python"] > 80])