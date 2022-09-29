# Basic error handling example
def foo1():
    try:
        value = int(input("value?"))
        print(f"{value} even? {value % 2 == 0}")
    except Exception as e:
        print(f"[ERROR] {e}")


# Example of error handling with else case
# Else block after try-except block is always run if the try block is successful
def foo2():
    while True:
        try:
            value = int(input("value?"))
            print(f"{value} even? {value % 2 == 0}")
        except Exception as e:
            print(f"[ERROR] {e}")
        else:
            print("Everything Done!")
            break


# Example of error handling with particular error cases
# Else block only runs if try block is successful
# Finally block runs irrespective of the outcome of the try-except block
def foo3():
    while True:
        try:
            x = int(input("x?"))
            y = int(input("y?"))
            print(f"x / y ? {x/y}")
        except ValueError as e:
            print(f"[ERR] {e}")
        except ZeroDivisionError as e:
            print(f"[ERR] {e}")
        else:
            print("Inside else-block...terminating program.....")
            break
        finally:
            print("Inside finally-block......")


# foo1()
# foo2()
foo3()
