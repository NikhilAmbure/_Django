import random
class Employee:

    # Python adds this as a default
    def __init__(self, name, designation, age) -> None:
        self.name = name
        self.designation = designation
        self.age = age
        self.emp_id = self.generate_employee_id()
    
    def generate_employee_id(self):
        return f"EMP-{random.randint(100, 999)}"

    def get_employee_details(self):
        print(f"""Employee details are:
              EMP ID : {self.emp_id}
              Name : {self.name}
              Age : {self.age}
              Designation : {self.designation}
            """)

    print("Employee class")


emp_1 = Employee("Nick", "Full Stack Dev", "21")
emp_1.get_employee_details()