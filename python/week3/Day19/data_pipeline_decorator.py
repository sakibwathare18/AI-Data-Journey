from functools import wraps

# Reusable decorator to log the start and end of pipeline steps
def log_step(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}\n")
        return result
    return wrapper


def load_data():
    print("Loading data...")
    return [10, 20, 30, 40, 50]


@log_step
def transform_data(data):
    # Example transformation: keep numbers as-is or apply basic processing
    return [x for x in data]


@log_step
def calculate_total(data):
    return sum(data)


# Running the pipeline
if __name__ == "__main__":
    raw_data = load_data()
    processed_data = transform_data(raw_data)
    total = calculate_total(processed_data)
    
    print(f"Total: {total}")