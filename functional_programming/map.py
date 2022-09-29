numbers = [10, 20, 33, 45, 67, 19, 0, 1, -99, 56, -56, 101]
words = ["hello", "world", "welcome", "to", "python", "programming"]


def odd_to_even(item):
    if item % 2 != 0:
        return item * 2
    return item


def even_to_odd(item):
    if item % 2 == 0:
        return item * 2 + 1
    return item


def capitalize(item):
    return item[0].upper() + item[1:]


# Map function takes a function and an iterable and returns a new list
# Map function is a pure function
even_numbers = list(map(odd_to_even, numbers))
odd_numbers = list(map(even_to_odd, numbers))
capitalized_words = list(map(capitalize, words))

print("results ->")
print(f"even_numbers: {even_numbers}")
print(f"odd_numbers: {odd_numbers}")
print(f"capitalized_words: {capitalized_words}")

print()

print(f"numbers: {numbers}")
print(f"words: {words}")
