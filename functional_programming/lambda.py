from functools import reduce

# Lambda functions are anonymous functions
# They are not defined anywhere except where they are used
# Lambda functions cannot be reused - ideally used for map(), filter() and reduce()

numbers = [1, 2, 3, 4, 5, 6]
more_numbers = [10, 20, 33, 45, 67, 19, 0, 1, -99, 56, -56, 101]
words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
items = [(0, 2), (39, 19), (45, 1), (-90, 23), (45, 100), (101, 3000), (56, 0)]

# Using lambda function with map()
squares = list(map(lambda x: x ** 2, numbers))
capitals = list(map(lambda word: word[0].upper() + word[1:], words))

# Using the lambda function with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, more_numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, more_numbers))

# Using lambda function with reduce()
n_sum = reduce(lambda x, item: x + item, numbers, 0)
factorial = reduce(lambda x, item: x * item, numbers, 1)
initials = reduce(lambda x, item: x + item[0], words, "")

# Using lambda function to sort on the basis of second item of tuple in sorted()
sorted_items = sorted(items, key=lambda x: x[1])

print(f"numbers: {numbers}")
print(f"more_numbers: {more_numbers}")
print(f"words: {words}")
print(f"items: {items}")

print()

print(f"squares: {squares}")
print(f"capitals: {capitals}")
print(f"even numbers: {even_numbers}")
print(f"odd numbers: {odd_numbers}")
print(f"sum(n): {n_sum}")
print(f"fact(n): {factorial}")
print(f"initials: {initials}")
print(f"sorted items: {sorted_items}")

