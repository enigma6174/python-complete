numbers = [10, 20, 33, 45, 67, 19, 0, 1, -99, 56, -56, 101]
words = ["hello", "world", "welcome", "to", "python", "programming"]


def odd(item):
    if item % 2 != 0:
        return item


def even(item):
    if item % 2 == 0:
        return item


def long_word(item):
    if len(item) > 10:
        return item


# Filter function takes a function and an iterable and returns a filtered list
# Filter function is a pure function
even_numbers = list(filter(even, numbers))
odd_numbers = list(filter(odd, numbers))
long_words = list(filter(long_word, words))

print("results ->")
print(f"even_numbers: {even_numbers}")
print(f"odd_numbers: {odd_numbers}")
print(f"long_words: {long_words}")

print()

print(f"numbers: {numbers}")
print(f"words: {words}")
