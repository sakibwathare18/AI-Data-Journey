from student import Student

class StudentManager:


    def __init__(self):

        self.students = []

    def add_student(self, student):
        self.students.append(student)

        print("Student Added Successfully.")

    def display_students(self):

        if len(self.students) == 0:
            print("No students found.")
            return
        for student in self.students:

            print("\n------------")
            student.display()

    def search_student(self, name):

        for student in self.students:

            if student.name.lower() == name.lower():

                student.display()
                return

        print("Student not found.")

    def delete_student(self, name):

        for student in self.students:

            if student.name.lower() == name.lower():
                self.students.remove(student)
                print("Student deleted successfully.")
                return

        print("Student not Found.")

    def statistics(self):

        if len(self.students) == 0:

            print("No students available.")
            return

        averages = [
            student.average()
            for student in self.students
        ]

        print("\n===== STATISTICS =====")

        print("Total students:", len(self.students))
        print("Highest average:", max(averages))
        print("Lowest average:", min(averages))
        print("Overall average:", sum(averages) / len(averages))

    def save_students(self):
        file_path = r"\\wsl.localhost\Ubuntu\home\sakib\AI-Data-Journey\python\week2\Day14\data\students.txt"

        with open(file_path,"w") as file:

            for student in self.students:
                student_text = f"{student.name},{student.age},{student.marks},{student.average()},{student.grade()}"
                file.write(student_text + "\n")

    def load_students(self):
        file_path = r"\\wsl.localhost\Ubuntu\home\sakib\AI-Data-Journey\python\week2\Day14\data\students.txt"

        self.students = []

        with open(file_path, "r") as file:

            for line in file:
                clean_line = line.strip()

                if not clean_line:
                    continue

                # Split only the first two commas
                name, age, remaining = clean_line.split(",", 2)

                # Extract marks from [90.0, 80.0, 70.0]
                marks_text = remaining.split("],", 1)[0] + "]"

                # Convert string list into actual Python list
                marks = eval(marks_text)

                student = Student(name, int(age), marks)

                self.students.append(student)