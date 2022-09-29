# List comprehension example
numbers = [i for i in range(10)]
squares = [i ** 2 for i in range(10)]
cubes = [i ** 3 for i in range(10)]

print(f"numbers {numbers}")
print(f"squares {squares}")
print(f"cubes {cubes}")

print()

# List comprehensions with conditions
even_numbers = [i for i in range(10) if i % 2 == 0]
even_squares = [i ** 2 for i in range(10) if (i ** 2) % 3 == 0]
string_list = [ch for ch in "PythOnProGRammINg" if ch.isupper()]

print(f"even numbers {even_numbers}")
print(f"3x squares {even_squares}")
print(f"string list {string_list}")

print()

d = {
    "k1": 20,
    "k2": 30,
    "k4": 5,
    "k5": 9,
    "k6": 19
}
print(f"d-original {d}")
print()

# Dictionary comprehension examples
d1 = {k: v ** 2 for k, v in d.items()}
d2 = {k: v ** 3 for k, v in d.items() if v % 3 == 0}
d3 = {k: v for k, v in zip(numbers, squares)}
d4 = {k: v for k, v in zip(numbers, zip(squares, cubes)) if k % 2 != 0}

print(f"d-squared {d1}")
print(f"d-cubed-3x {d2}")
print(f"d-zip-number-square {d3}")
print(f"d-zip-number-zip-square-cube-odd {d4}")
