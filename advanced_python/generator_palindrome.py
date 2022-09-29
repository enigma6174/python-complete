def is_palindrome(num):
    # Ignore single digit numbers
    if num // 10 == 0:
        return False

    # Temporary variable to reverse the original number
    temp = num
    # Variable to store current reversed number
    reversed_num = 0

    # Algorithm to reverse the number
    # In each iteration remove the last digit of original number
    # Append each removed digit after the current digit of reversed number
    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    # Check for palindrome
    if num == reversed_num:
        return True
    else:
        return False


# Generator function to return infinite palindromes
def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            x = (yield num)
            if x is not None:
                num = x
        num += 1


palindrome_generator = infinite_palindromes()
for i in palindrome_generator:
    print(i)
    digits = len(str(i))
    palindrome_generator.send(10 ** digits)
