from basics2 import Employee
from basics2 import display, status, modify


e1 = Employee("John Doe", "Legal")
e2 = Employee("Herbert Schildt", "IT")

display(e1)
display(e2)

print("[INFO] DISPLAY WITH OBJECT")
status(e1)

print("[INFO] DISPLAY WITH CLASS")
status(Employee)

print(">>>> MODIFYING STATUS <<<<\n")
modify(e1)

print("[INFO] USER__DATA AFTER UPDATE\n")

display(e1)
display(e2)

print("[INFO] DISPLAY WITH CLASS")
status(Employee)

print(">>>> MODIFYING STATUS <<<<\n")
modify(Employee)

print("[INFO] USER__DATA AFTER UPDATE\n")

display(e1)
display(e2)

print("[INFO] DISPLAY WITH CLASS")
status(Employee)

print(">>>> MODIFYING STATUS <<<<\n")
modify(Employee)

display(e1)
display(e2)

e3 = Employee("Cindy Larson", "Research")

display(e3)
status(e3)

print(">>>> MODIFYING STATUS <<<<\n")
modify(Employee)

display(e3)
status(Employee)

e4 = Employee.generate_employee("Laurel", "Marketing")

display(e4)
status(e4)

print(f"COMPANY__NAME: {e4.get_company_name()}")
print(f"OBJECT__DATA: {e4.get_object()}\n")

print(f"COMPANY__NAME: {Employee.get_company_name()}")
