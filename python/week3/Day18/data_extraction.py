import re

text = """
Name: Sakib, Age: 21
Name: Rahul, Age: 22
Name: Amit, Age: 20
"""

pattern = r"Name:\s(\w+),\sAge:\s(\d+)"
data = re.findall(pattern, text)

print(data)