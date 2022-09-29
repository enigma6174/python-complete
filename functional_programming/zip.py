words = ["hello", "world", "welcome", "to", "python", "programming"]
word_lengths = [len(word) for word in words]

primes = (2, 3, 5, 7, 11, 13, 17, 19)
sentences = ("welcome to python programming", "hello world", "today is a good day")

# Zip function takes two or more lists and combines individual items of the lists into a tuple
# The final return value of zip() is  a tuple of the items of the combined lists
# Zip function is a pure function
result = list(zip(words, word_lengths))
print(f"(word, word_length): {result}")

print()

# When the number of items in an iterable is less then zip() only combines the lesser number of items together
result = list(zip(primes, sentences))
print(f"f(prime, sentence): {result}")

print()

print(f"primes: {primes}")
print(f"sentences: {sentences}")
print(f"words: {words}")

print()

# It is possible to zip iterables of different types
# When multiple iterables are provided the one with the smallest length is the length of zip()
result = list(zip(primes, sentences, words))
print(f"(prime, sentence, word): {result}")

# When a string is used as an argument to zip() it is broken down into characters for zipping
result = list(zip(primes, "PRIME"))
print(f"(prime, 'PRIME'): {result}")
