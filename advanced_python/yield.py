# In generator functions yield is used in place of return
# Unlike return yield does not stop the execution of the function
# Yield suspends the function preserving it's state and returns the value to the caller
def sequence():
    num = 10
    while True:
        num += 3
        yield num
        num += 10


# Return the object from generator function
g = sequence()

# Every time next() is called on g() the code till yield is run
# The current function state is suspended
# The code after yield is run in the following next() call
# The next iteration of code till yield will also be run with the latest values
# Output will be 13
print(f"ITER_1 {next(g)}")

# This is the second iteration so current value of num will be 13
# The line after yield will be executed and num will be updated to 23
# The latest iteration of next will update num to 26 and return
print(f"ITER_2 {next(g)}")

# This is the third iteration so both print() statements will get executed
# Value of a will be 39
print(f"ITER_3 {next(g)}")
print()


# Yield statements are exhaustible
# We can use as many next() statements on the generator as there are yields in the generator function
def multi_yield():
    string = "hello"
    yield string

    string += " world"
    yield string

    string += "!\n"
    yield string

    string += "Welcome To Python Programming"
    yield string


g = multi_yield()

# First yield call
print(f"ITER_1\n{next(g)}")

# Second yield call
print(f"ITER_2\n{next(g)}")

# Third yield call
print(f"ITER_3\n{next(g)}")

# Last yield call
print(f"ITER_4\n{next(g)}")

# If we use next() on a generator more number of times than yields exception is raised
try:
    print(f"ITER_5 {next(g)}")
except StopIteration:
    print("")


def number_generator(n):
    number = 0
    while number < n:
        yield number
        number += 1


generator = number_generator(3)

# Generating values using next()
for i in range(4):
    try:
        print(f"{next(generator)}")
    except StopIteration:
        print("")

x = number_generator(5)

# Generate values by wrapping the generator in list()
values = list(x)
print(values)
