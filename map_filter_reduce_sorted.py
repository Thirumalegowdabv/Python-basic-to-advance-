# maps (), filter() , reduce (), sorted ()

# these are global functions udes for collections 
# these are higher-order functions in Python that work beautifully with lambda functions.



# map()

# Applies a function to every item in an iterable (list, tuple, etc.) and returns a new iterator.

# Syntax:
# map(function, iterable)

nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print(squares)   # [1, 4, 9, 16, 25]




# filter()

# Filters elements of an iterable based on a condition (True/False).

# Syntax:

# filter(function, iterable)

nums = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)   # [10, 20, 30]




# sorted()

# Returns a new sorted list from an iterable.
# You can pass a key function to customize sorting.

# Syntax:

# sorted(iterable, key=None, reverse=False)

# Example 1 – Numbers:

nums = [5, 2, 9, 1, 7]
print(sorted(nums))            # [1, 2, 5, 7, 9]
print(sorted(nums, reverse=True))  # [9, 7, 5, 2, 1]


# Example 2 – Sorting with key:

students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
# Sort by age
print(sorted(students, key=lambda x: x[1]))
# [('Bob', 20), ('Charlie', 23), ('Alice', 25)]




# reduce()

# Reduces an iterable to a single value by repeatedly applying a function.
# Comes from functools module.

# Syntax:

# reduce(function, iterable)

# Example 1 – Sum of numbers:

from functools import reduce

nums = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, nums)
print(total)   # 15


# Example 2 – Product of numbers:

product = reduce(lambda x, y: x * y, nums)
print(product)   # 120