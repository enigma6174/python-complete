from functools import reduce

# Input list for reduce() method
numbers = [1, 2, 3, 4, 5]
words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

# Input tuple for reduce() method
primes = (2, 3, 5, 7, 11, 13, 17, 19)
sentences = ("welcome to python programming", "hello world", "today is a good day")


# Accumulator function for reduce() method
# Returns a single value
def accumulator_add(acc, item):
    return acc + item


def accumulator_mult(acc, item):
    return acc * item


def accumulator_word(acc, item):
    return acc + item[0]


def accumulator_prime(acc, item):
    if item < 10:
        return acc - item
    return acc + item


def accumulator_sentence(acc, item):
    buffer = item.split(" ")
    temp = reduce(accumulator_word, buffer, "")
    return acc + "$" + temp


# Reduce method reduces an iterable to a single value
# It takes an input function for reduction, the iterable to reduce and a starting value
# Reduce method is a pure function
result_add = reduce(accumulator_add, numbers, 0)
result_mult = reduce(accumulator_mult, numbers, 1)
result_word = reduce(accumulator_word, words, "")

print(f"numbers: {numbers}")
print(f"reduce(numbers): {result_add}\n")

print(f"numbers: {numbers}")
print(f"reduce(numbers): {result_mult}\n")

print(f"numbers: {words}")
print(f"reduce(numbers): {result_word}\n")

print()

# Applying reduce() on tuples
prime_reduce = reduce(accumulator_prime, primes, 0)
sentence_reduce = reduce(accumulator_sentence, sentences, "")

print(f"numbers: {primes}")
print(f"reduce(numbers): {prime_reduce}\n")

print(f"numbers: {sentences}")
print(f"reduce(numbers): {sentence_reduce}\n")
