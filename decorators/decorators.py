def outer(f):

    # Inner function inside outer() that calls the argument f()
    # The return value of outer() is a reference to inner()
    def inner():
        print("\ninside inner() ->")
        f()

    return inner


def hello():
    print("hello world!")


def greet():
    print("good day!")


# Call the function using the standard way
hello()
greet()

# Call the function using the decorator function
h = outer(hello)
h()

g = outer(greet)
g()


# The syntax to create decorator is same as above
# An outer function that takes a function as argument and returns a wrapper function
# The wrapper function provides additional functionalities and calls the argument function
# The outer function is the decorator
def my_decorator(f):

    # Wrapper function which calls the argument function f()
    def wrapper():
        print("\n@my_decorator")
        f()

    return wrapper


# Using the decorator to define hello() with functionalities of wrapper()
@my_decorator
def hello():
    print("hello world")


# Using the decorator to define greet() with functionalities of wrapper()
@my_decorator
def greet():
    print("good day!")


def bye():
    print("goodbye!")


# Not using the decorator but gives the same result
b = my_decorator(bye)

hello()
greet()
b()

