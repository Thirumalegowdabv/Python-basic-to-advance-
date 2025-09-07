#  Decorators

# A decorator is a function that takes another function as input and extends or modifies its behavior, without changing the original function’s code.

# Think of it as “wrapping” a function with extra functionality.



# Functions are First-Class Citizens

# In Python:

# You can pass functions as arguments.

# You can return functions from functions.

# You can store functions in variables.

# Example:

def greet(name):
    return f"Hello, {name}"

say_hello = greet
print(say_hello("Alice"))   # Hello, Alice



# Basic Decorator Example
def decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@decorator   # Same as: say_hello = decorator(say_hello)
def say_hello():
    print("Hello!")

say_hello()


# Output:

# Before function runs
# Hello!
# After function runs




# Practical Use Cases
# (a) Logging
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log
def multiply(a, b):
    return a * b

print(multiply(3, 4))

# (b) Authentication
def require_admin(func):
    def wrapper(user):
        if user != "admin":
            print("Access Denied")
        else:
            func(user)
    return wrapper

@require_admin
def delete_database(user):
    print("Database deleted!")

delete_database("guest")  # Access Denied
delete_database("admin")  # Database deleted!

# (c) Timing Function Execution
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} sec")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Finished!")

slow_function()




# Chaining Multiple Decorators
def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

def exclaim(func):
    def wrapper():
        return func() + "!!!"
    return wrapper

@exclaim
@uppercase
def greet():
    return "hello"

print(greet())   # HELLO!!!




# Built-in Decorators

# @staticmethod → defines static methods.

# @classmethod → defines class methods.

# @property → creates getter/setter.

# Example:

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

p = Person("Alice")
print(p.name)   # Alice

