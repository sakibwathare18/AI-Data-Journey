class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def average(self):

        if len(self.marks) == 0:
            return 0

        return sum(self.marks)/len(self.marks)

    def grade(self):
        avg = self.average()

        if avg >= 90:
            return "A"

        elif avg >= 75:
            return "B"

        elif avg >= 60:
            return "C"

        elif avg >= 40:
            return "D"

        else:
            return "F"

    def display(self):

        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Marks : {self.marks}")
        print(f"Average : {self.average():.2f}")
        print(f"Grade : {self.grade()}")

