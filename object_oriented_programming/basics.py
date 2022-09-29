class Player:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def run(self):
        print(f"{self.email}> {self.username} has joined the party!")

    def len(self):
        return len(self.__dict__.items())


class Toy:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return len(self.__dict__.items())
