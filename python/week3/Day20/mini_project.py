import re
from functools import wraps


# -----------------------------
# Raw Data
# -----------------------------

records = [
    "Sakib,21,sakib@gmail.com,9876543210",
    "Rahul,22,rahul@gmail.com,9123456780",
    "Amit,17,amit@gmail.com,9988776655",
    "Invalid Data",
    "Neha,23,neha@gmail.com,9876501234",
    "Priya,25,invalid-email,9876501111"
]


# -----------------------------
# Decorator
# -----------------------------

def log_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Running: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


# -----------------------------
# Step 1: Extract
# -----------------------------

@log_function
def extract(records):
    for record in records:
        parts = record.split(",")

        if len(parts) == 4:
            yield parts


# -----------------------------
# Step 2: Validate
# -----------------------------

@log_function
def validate(records):
    email_pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
    phone_pattern = r"^\d{10}$"

    for record in records:

        name, age, email, phone = record

        # Validate name
        if not name.strip():
            continue

        # Validate age
        try:
            age = int(age)
        except ValueError:
            continue

        # Validate email
        if not re.match(email_pattern, email):
            continue

        # Validate phone
        if not re.match(phone_pattern, phone):
            continue

        yield name, age, email, phone


# -----------------------------
# Step 3: Transform
# -----------------------------

@log_function
def transform(records):
    for name, age, email, phone in records:

        transformed_record = {
            "name": name.lower(),
            "age": age,
            "email": email.lower(),
            "phone": phone
        }

        yield transformed_record


# -----------------------------
# Step 4: Filter
# -----------------------------

@log_function
def filter_records(records):
    for record in records:

        if record["age"] >= 18:
            yield record


# -----------------------------
# Step 5: Output
# -----------------------------

@log_function
def process_records(records):

    extracted = extract(records)

    validated = validate(extracted)

    transformed = transform(validated)

    filtered = filter_records(transformed)

    for record in filtered:
        yield record


# -----------------------------
# Main Program
# -----------------------------

if __name__ == "__main__":

    print("\n--- FINAL OUTPUT ---")

    for record in process_records(records):
        print(record)