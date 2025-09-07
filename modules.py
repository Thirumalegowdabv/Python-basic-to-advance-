# A module is simply a Python file (.py) that contains code (functions, classes, or variables) which you can import and use in another program.
# It helps in code reusability and organization.

# Example:

# math.py (module) contains math functions.

# You can use it in your program by import math.


# Types of Modules

# Built-in Modules → Already included in Python (e.g., math, os, random).

# User-defined Modules → Created by you.

# External Modules → Installed using pip (e.g., numpy, pandas).



# Using Built-in Modules

# Example with math:

import math

print(math.sqrt(16))   # 4.0
print(math.factorial(5))  # 120
print(math.pi)   # 3.141592653589793


# Importing with alias

import math as m
print(m.sqrt(25))  # 5.0


# Importing specific functions

from math import sqrt, pi
print(sqrt(36))  # 6.0
print(pi)        # 3.141592653589793

# Creating a User-defined Module

# Create a file mymodule.py:
# Use it in another file main.py:



# Useful Built-in Modules

# os → file system operations.

# sys → system-specific parameters.

# random → random numbers.

# datetime → date/time.

# json → work with JSON.

# collections → advanced data structures.

# itertools → iterators, combinations, permutations.