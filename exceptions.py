# Exceptions

# An exception is an error that occurs during the execution of a program.

# Instead of the program crashing, Python lets you handle these errors gracefully.

# Example (without handling):

print("Start")
x = 10 / 0   # Division by zero
print("End")


# Output:

# ZeroDivisionError: division by zero
# The program stops immediately when the error occurs.




# 2. Handling Exceptions (try-except)

# We use a try-except block:

try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")


# Output:
# You can't divide by zero!

# try: code that may cause an error.
# except: code that runs if an error happens.




# 3. Catching Multiple Exceptions

# You can handle different errors separately:

try:
    num = int("abc")  # ValueError
    x = 10 / 0        # ZeroDivisionError
except ValueError:
    print("Invalid conversion to integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")


# Or catch multiple exceptions in one block:

try:
    num = int("abc")
except (ValueError, TypeError):
    print("Error: wrong data type.")



# 4. Using else and finally

# else: runs if no exception occurs.
# finally: runs always, whether an error happened or not.

try:
    x = 10 / 2
except ZeroDivisionError:
    print("Division error")
else:
    print("Division successful, result:", x)
finally:
    print("This will always run.")

# Output:
# Division successful, result: 5.0
# This will always run.



# 5. Raising Exceptions

# You can manually raise errors with raise.

x = -5
if x < 0:
    raise ValueError("x cannot be negative")



# 6. Custom Exceptions

# We can create our own exception classes (advanced use).

class NegativeNumberError(Exception):
    pass

def check_number(n):
    if n < 0:
        raise NegativeNumberError("Negative numbers not allowed!")
    else:
        print("Valid number:", n)

try:
    check_number(-10)
except NegativeNumberError as e:
    print("Caught custom exception:", e)
    
    
    
    
    
# Best Practices

#  Catch specific exceptions (not just except:).
#  Use finally for cleanup tasks (e.g., closing files).
#  Define custom exceptions only when needed.
#  Avoid swallowing errors silently.



#  Advanced – Exception Chaining

# Python allows chaining exceptions using raise ... from ....

try:
    int("abc")
except ValueError as e:
    raise RuntimeError("Conversion failed") from e

# This preserves the original cause of the error.


#  Advanced – Context Managers & Exceptions

# When working with files or resources, we often use context managers (with), which handle exceptions automatically.

try:
    with open("file.txt") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found!")











































