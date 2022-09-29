from time import time


def decorator(f):

    def wrapper(*args, **kwargs):
        f(*args, **kwargs)

    return wrapper


@decorator
def greet(message, name="user"):
    print(f"{message} {name}")


greet("hi", "john")
greet("welcome")


def performance(f):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = f(*args, **kwargs)
        t2 = time()
        print("runtime: %.3f" % (t2 - t1), "seconds")
        return result
    return wrapper


print()


@performance
def list_append(n):
    buffer = []
    for i in range(n):
        buffer.append(i)


@performance
def list_comprehension(n):
    buffer = [i for i in range(n)]


print("performance of list append on 1 million items ->")
list_append(1000000)

print()

print("performance of list comprehension on 1 million items ->")
list_comprehension(1000000)
