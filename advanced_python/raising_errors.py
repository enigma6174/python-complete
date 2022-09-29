# A simple example of raising an exception
def f(x, y):
    if y == 0:
        raise Exception(f"Cannot divide by zero!")
    return x / y


# A more in-depth example of raising exception
def g(y):
    try:
        if y == 0:
            raise Exception(f"[EXC] Cannot divide by zero!")
        x = int(input("input?"))
    except ValueError as value_error:
        raise Exception(f"[VAL_ERR] {value_error}")
    else:
        return x / y


# All code that raise exceptions must be called from try-except block
try:
    value = f(20, 0)
    print(value)
except Exception as e:
    print(f"[ERR] {e}")

print()

# The code runs but stops execution after error because exception has been raised but not caught
# Uncomment the code to check
# print(f(20, 0))


# Exceptions that are not raised will get caught in the try-except block
# Exceptions that are raised will display the custom error-handling behavior
try:
    result = g(5)
    print(result)
except Exception as e:
    print(f"[X] Exception Caught (Not Raised): {e}")
