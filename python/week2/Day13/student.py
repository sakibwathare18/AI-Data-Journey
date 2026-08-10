class Student:
    def __init__(self, name, marks=None):
        self.name = name
        self.marks = marks if marks is not None else []

    def display(self):
        print("Name  :", self.name)
        print("Marks :", self.marks)

    def average(self):
        if not self.marks:
            return 0
        
        # Calculate and return the mathematical average
        return sum(self.marks) / len(self.marks)

    def grade(self):
        # Call average calculation internally without duplicating print statements
        avg = self.average()

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"


# --- Execution Block ---
stud = Student("Sakib", [80, 90, 30])

stud.display()

# Calculate, format to 2 decimal places, and print the average once
avg_score = stud.average()
print(f"Average : {avg_score:.2f}")

grd = stud.grade()
print("Grade   :", grd)
