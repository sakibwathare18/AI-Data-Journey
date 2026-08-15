import re

text = """
Hello, my name is Sakib.
My email is sakib@gmail.com.
You can call me at 9876543210.

I am learning #Python, #DataScience and #AI.

My GitHub is https://github.com/sakibwathare18
"""

name_match = re.search(r"name is ([A-Za-z]+)",text)
email_match = re.search(r"[\w\.-]+@[\w\.-]+.\w+",text)
phone_match = re.search(r"\b\d{10}\b",text)
hashtags = re.findall(r"#\w+",text)
github_match = re.search(r"https://github.com/\w+",text)

print("Name:\n",name_match.group(1))
print("Email:\n",email_match.group())
print("Phone:\n",phone_match.group())
print("Hashtags:\n","\n".join(hashtags))
print("GitHub:\n",github_match.group(0))