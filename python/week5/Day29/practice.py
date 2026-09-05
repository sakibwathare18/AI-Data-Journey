import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Sneha", "Rahul", "Priya", "Vikas"],
    "Python": [85, 92, 76, 88, 69],
    "SQL": [78, 89, 82, 91, 74],
    "ML": [81, 95, 72, 86, 67],
    "Experience": [1, 2, 1, 3, 2]
}

df = pd.DataFrame(data)

# print(df)

#Top 3
# print(df.head(3))

#Last 2
# print(df.tail(2))

#Only Name, Python, SQL
# print(df[["Name","Python","SQL"]])

#SQL > 80 AND ML > 80
# print(df[
#     (df["SQL"] > 80) &
#     (df["ML"] > 80)
# ])

#employees with more than 1 year experience
# print(df.loc[df['Experience'] > 1, ['Name', 'Experience']])

print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())