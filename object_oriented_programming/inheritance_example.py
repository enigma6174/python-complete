from inheritance import Employee, Developer, Manager


dev1 = Developer("BACKEND", "ML_DASHBOARD", "JOHN", "JDOE_92@EMAIL.COM")
dev2 = Developer("CLOUD", "DB_WEBAPP", "LINDA", "LINDACRAWFORD_888@EMAIL.COM")

dev1.get_data()
dev1.work()
print(f"ID({dev1.name}): {dev1.get_id()}\nREGISTERED? {dev1.is_registered()}\n")

dev2.get_data()
dev2.work()
print(f"ID({dev2.name}): {dev2.get_id()}\nREGISTERED? {dev2.is_registered()}\n")

mgr1 = Manager("AI", "BANGALORE", "DARCY", "DARCT232@EMAIL.COM")
mgr2 = Manager("MARKETING", "NEW YORK", "MARK", "MARK444@EMAIL.COM")

mgr1.get_data()
mgr1.work()
print(f"ID({mgr1.name}): {mgr1.get_id()}\nREGISTERED? {mgr1.is_registered()}\n")

mgr2.get_data()
mgr2.work()
print(f"ID({mgr2.name}): {mgr2.get_id()}\nREGISTERED? {mgr2.is_registered()}\n")

janitor = Employee("HENRY", "HENRY_JANITOR@EMAIL.COM")
print(f"{janitor.get_id()} # {janitor.get_data()}")
janitor.work()

print("=" * 50)

print(f"isinstance(dev1, Developer)? {isinstance(dev1, Developer)}")
print(f"isinstance(dev2, Employee)? {isinstance(dev2, Employee)}")
print(f"isinstance(mgr1, Manager)? {isinstance(mgr1, Manager)}")
print(f"isinstance(mgr2, Employee)? {isinstance(mgr2, Employee)}")
print(f"isinstance(dev1, Manager)? {isinstance(dev1, Manager)}")
print(f"isinstance(mgr1, Developer)? {isinstance(mgr1, Developer)}")
print(f"isinstance(janitor, Employee)? {isinstance(janitor, Employee)}")
