class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def category(self):
        if self.salary >= 70000:
            return "High Salary"
        elif self.salary >= 40000:
            return "Medium Salary"
        else:
            return "Low Salary"

    def display(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Salary: ₹", self.salary)
        print("Category:", self.category())
        print("------------------------")


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        print("\nEmployee Details")
        print("========================")

        for employee in self.employees:
            employee.display()


# Creating Company object
company = Company()

# Taking employee details
n = int(input("Enter number of employees: "))

for i in range(n):
    print("\nEnter details of Employee", i + 1)

    employee_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    salary = float(input("Enter Salary: "))

    employee = Employee(employee_id, name, salary)

    company.add_employee(employee)

# Display all employees
company.display_employees()