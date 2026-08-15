import re

text = """
Hello   Python

I am learning   Data Science.
"""

clean_txt = re.sub(r"\s+"," ",text)
print(clean_txt)