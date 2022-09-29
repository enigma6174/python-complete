class SuperList(list):

    def __len__(self):
        return 1000


a = SuperList([10, 20, 30, 40, 50])
print(a)

a.append(100)
a.append(999)
print(a)

print(len(a))
