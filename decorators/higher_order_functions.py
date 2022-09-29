# A function that takes another function as argument is higher order function
def f(g):
    g()


def x():
    print("Higher Order Function When Function Is Passed As Argument")


# Calling the higher order function
f(x)


# A function that returns another function is a higher order function
def foo():
    def fun():
        return "Higher Order Function When Function Is Returned As A Value"

    return fun


# Calling the higher order function
result = foo()
print(result())
print()


# A more realistic example
def power_builder(e):

    def power(value):
        return value ** e

    return power


# The returned function is used to create a square function
square = power_builder(2)

print(f"square(5): {square(5)}")
print(f"square(11): {square(11)}")

# The returned function is used to create a cube function
cube = power_builder(3)

print(f"cube(9): {cube(9)}")
print(f"cube(12): {cube(12)}")

# The returned function is used to create a square root function
square_root = power_builder(0.5)

print(f"square_root(169): {square_root(169)}")
print(f"square_root(625): {square_root(625)}")

