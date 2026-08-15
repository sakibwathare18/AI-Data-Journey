import re

logs = """
2026-08-15 INFO User logged in
2026-08-15 ERROR Database failed
2026-08-15 WARNING Memory high
2026-08-15 ERROR File missing
2026-08-15 INFO Process completed
"""

date_pattern = r"\d+-\d+-\d+"
date = re.findall(date_pattern,logs)
print(date)

logs_pattern = r"\d+-\d+-\d+\s([A-Z]+)"
logs = re.findall(logs_pattern,logs)
print(logs)

error_msg_pattern = r"ERROR\s(.+)"
errors = re.findall(error_msg_pattern, logs)
print(errors)