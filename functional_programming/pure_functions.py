numbers = []


# Impure function - affects the data on the outside world
# Impure functions are not guaranteed to return the same data for the same input everytime
def impure_double(n):
    numbers.append(n * 2)


# Pure function - does not affect the data on the outside world
# Pure functions are guaranteed to return the same data for the same input everytime
def pure_double(n):
    buffer = [n * 2]
    return buffer


# Impure function demo
print("impure function ->")
for i in range(3):
    impure_double(10)
    print(f"iteration: {i} input: 10 output: {numbers}")

print()

# Pure function demo
print("pure function ->")
for i in range(3):
    result = pure_double(10)
    print(f"iteration: {i} input: 10 output: {result}")
