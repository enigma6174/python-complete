from random import random


class Employee:

    registered = True

    def __init__(self, name, email):
        self.id = "@" + str(random()).split(".")[1]
        self.name = name
        self.email = email

    def get_id(self):
        return self.id

    def get_data(self):
        return f"{self.name} # {self.email}"

    @staticmethod
    def work():
        print("WORKING!")


class Developer(Employee):

    def __init__(self, team, project, name, email):
        super().__init__(name, email)
        self.team = team
        self.project = project

    def get_data(self):
        print(f"{super().get_data()} WORKING ON {self.project} PROJECT WITH {self.team} TEAM")

    @staticmethod
    def work():
        print("WRITING CODE!")

    @staticmethod
    def is_registered():
        return Employee.registered


class Manager(Employee):

    def __init__(self, unit, location, name, email):
        super().__init__(name, email)
        self.unit = unit
        self.location = location

    def get_data(self):
        print(f"{super().get_data()} MANAGES {self.unit} UNIT FOR {self.location} LOCATION")

    @staticmethod
    def work():
        print("ORGANIZING MEETING!")

    @staticmethod
    def is_registered():
        return Employee.registered
