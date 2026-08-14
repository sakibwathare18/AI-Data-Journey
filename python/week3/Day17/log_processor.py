logs = [
    "INFO User logged in",
    "ERROR Database connection failed",
    "INFO Data loaded",
    "WARNING Memory usage high",
    "ERROR File not found",
    "INFO Process completed"
]

def error_log(logs):
    for log in logs:
        if "ERROR" in log:
            yield log

def info_log(logs):
    for log in logs:
        if "INFO" in log:
            yield log

error = error_log(logs)
info = info_log(logs)
for i in error:
    print(i)
for i in info:
    print(i)