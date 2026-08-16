import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start_time = time.perf_counter()
        result = func(*args,**kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Result: {result}")
        print(f"Execution Time: {execution_time}")
        return result
    return wrapper

@timer
def process_data():
    total = 0
    for i in range(1000000):
        total += i
    return total

print(process_data())