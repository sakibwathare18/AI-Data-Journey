class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def display(self):
        print("--Employee Details--")
        print(f"Name : {self.name} \nSalary : {self.salary} \nDepartment : {self.department}")

    def annual_salary(self):
        print(f"Annual Salary : {self.salary*12}")

emp = Employee("Sakib",50000,"Amazon")

emp.display()
emp.annual_salary()