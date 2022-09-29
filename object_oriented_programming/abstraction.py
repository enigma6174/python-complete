class User:

    def __init__(self, user_name, email_id):
        self._username = user_name
        self._email = email_id

    def _hello(self):
        print(f"WELCOME {self._username}!")

    def create_user(self):
        print(f"USER {self._username} EMAIL {self._email} CREATED!")
        self._hello()


user1 = User("jdoe22", "johndoe22@email.com")
user1.create_user()

print("\n[INFO] UPDATING....\n")

user1._username = "johndoe22"
user1._email = "johndoe22@email.com"
user1.create_user()
