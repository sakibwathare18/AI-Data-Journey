import re

text = """
python 3
Java 17
C++ 20
SQL 2024
"""

number = re.findall(r"\d")
print(number.group())

text = """
Sakib: 9876543210
Rahul: 9123456780
Amit: 9988776655
"""

number = re.findall(r"\d{10}",text)
print(number)

text = """
sakib@gmail.com
rahul@yahoo.com
amit123@outlook.com
"""

pattern = r"\w+@\w+\.\w+"
email = re.findall(pattern,text)
print(email)

text = """
#Python #DataScience #MachineLearning #AI
"""

hashtags = re.findall(r"#\w+",text)
print(hashtags)