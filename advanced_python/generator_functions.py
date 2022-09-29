# Generate a sequence of numbers using regular approach
def range_sequence(n):
    for num in range(n):
        print(num, end=" ")
    print()


# Generate a sequence of numbers using generators
def generate_sequence(n):
    num = 0
    while num < n:
        yield num
        num += 1


# Method to generate infinite sequence using generator
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


# Calling the range_sequence(n) method
print("calling range_sequence(10)...")
range_sequence(10)

# Calling the generate_sequence(n) method will not have any effect
print("\ncalling generate_sequence(10)...")
generate_sequence(10)

print()

# To use the values from generate_sequence(n) we need to use an iterator
# Iterate over the generate_sequence(n) to print the values
print("iterating over generate_sequence(10)...")
for i in generate_sequence(10):
    print(i, end=" ")

print()

# Generate an infinite sequence of numbers
# Requires keyboard interrupt to stop the code
# for i in infinite_sequence():
#     print(i, end=" ")

print("\ngenerator objects: ")

# Generator function returns an object
g = generate_sequence(15)
print(g)
print()

# Using next() on the generator object we can get each value that was generated
print(f"ITER=1 VAL={next(g)}")
print(f"ITER=2 VAL={next(g)}")
print(f"ITER=3 VAL={next(g)}")
print()


# Using next() on generator of infinite sequence to generate a finite sequence
def finite(n):
    it = infinite_sequence()
    count = 0
    while count < n:
        value = next(it)
        count += 1
        print(f"ITER={count} VAL={value} MEM={id(value)}")


print("generating a sequence in (0, 15) from infinite_sequence()\n")
finite(10)
