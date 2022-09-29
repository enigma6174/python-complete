from basics import Player, Toy


player = Player("johnDoe", "john_doe29@email.com")

flag = False

# Avoiding the loop output every time this script is run
if flag:
    for item in dir(player):
        print(item)

# Reference to the same object
obj = player
print(obj)

# String representation of object
obs = player.__str__()
print(obs)

# This will work because player is still object
obj.run()

# This will not work because player.__str__() is not object
# obs.run()

# Get the object represented as dictionary
print(player.__dict__)

# Regular method len() has been added to the class
print(player.len())

# Since len() is not dunder method cannot call it as len(player)
# print(len(player))

print("=" * 100)

toy = Toy("red")

print(f"toy: {toy}")
print(f"str(toy): {str(toy)}")
print(f"toy.__str__(): {toy.__str__()}")

# Dunder method __len__() has been added to the class
# Since __len__() is dunder method both ways can be used to call
print(f"toy.__len__(): {toy.__len__()}")
print(f"len(toy): {len(toy)}")
