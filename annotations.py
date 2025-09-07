# Annotations
# Annotations in Python are a way to add metadata (extra information) to function parameters and return values.
# They do not affect the execution of the code — they are only hints.
# Mostly used for type hints.

#  Basic Example
def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))   # 5


# a: int → parameter a is expected to be an integer

# b: int → parameter b is expected to be an integer

# -> int → function will return an integer

# But Python won’t enforce types:

print(add("Hello", "World"))   # HelloWorld (no error)

# It’s only a hint, not a rule.


# Why Use Annotations?

# Improves readability of code
# Helps with IDE auto-completion
# Used in static type checkers (like mypy, pyright)
# Useful in big projects & teamwork