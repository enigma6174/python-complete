# Generators can be built with generator function
# Generator function uses yield instead of return statement
# Code can follow a yield statement
# The return value of a generator function is always a generator object
# Need to use iterator or next() to generate the values
def sequence():
    num = 0
    while True:
        yield num
        num += 1


# Generator object returned by the generator function
g = sequence()

# Using next() to generate values of generator object g
print("generator function...")
for i in range(5):
    print(f"i={i} val={next(g)}")


# Generators can be built using generator comprehension
# Generator comprehensions are enclosed in () instead of []
# Generator comprehensions always return a generator object
# Need to use iterator or next() to generate the values
# Generator expression to generate squares of numbers from (1, 11)
squares = (number ** 2 for number in range(1, 11))

# Using iterator over generator object squares to generate values
print("\ngenerator comprehension...")
count = 1
for square in squares:
    print(f"square({count})={square}")
    count += 1

