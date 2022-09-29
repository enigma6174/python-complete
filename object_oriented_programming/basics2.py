from random import random


class Employee:
    # Class attribute
    is_employee = True

    # Constructor with object attribute
    def __init__(self, name, dept):
        self.emp_id = str(random()).split(".")[1]
        self.emp_name = name
        self.emp_dept = dept

    # Method
    def get_employee_data(self):
        return f"{self.emp_name} works in {self.emp_dept} department"

    # Method
    def get_employee_id(self):
        return f"{self.emp_id}"

    # Method
    def get_object(self):
        return self

    # Class Method
    @classmethod
    def generate_employee(cls, emp_name, emp_dept):
        return cls(emp_name, emp_dept)

    # Class Method
    @classmethod
    def update_status(cls):
        cls.is_employee = not cls.is_employee

    # Static Method
    @staticmethod
    def status():
        return Employee.is_employee

    # Static Method
    @staticmethod
    def get_company_name():
        return "Abacus Technologies"


# Display user data from the object
def display(self):
    print(f"@{self.get_employee_id()}__DATA: {self.get_employee_data()}")
    print(f"@{self.get_employee_id()}__STATUS: {self.status()}\n")


# Display class variable contents
def status(self):
    print(f"EMPLOYEE__STATUS: {self.is_employee}\n")


# Modify class variable using object
def modify(self):
    self.update_status()
