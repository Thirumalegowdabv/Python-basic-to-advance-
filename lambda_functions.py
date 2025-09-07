# Lambda functions

# A lambda function is a small, anonymous (nameless) function in Python.
# It is defined using the keyword lambda.
# Used when you need a short function for a short time.

# lambda arguments: expression

lambda num : num*2


# Multiple Arguments
mul = lambda a, b : a * b
print(mul(4,5))

# Normal function:
def square(x):
    return x * x

# Lambda function:
square = lambda x: x * x
print(square(5))   # 25

# Conditional in Lambda

max_num = lambda a, b: a if a > b else b
print(max_num(10, 20))   # 20

# Nested Lambda
multiply = lambda x: (lambda y: x * y)
result = multiply(5)(3)
print(result)   # 15


# When to Use Lambda?

#  When you need a short function for a single-use case.
#  When passing functions as arguments (map, filter, sorted, reduce).
#  Don’t use lambda for long, complex logic (use def instead).

# Lambda functions are very useful with higher-order functions like map(), filter(), and sorted().

# map() → Apply function to all items
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print(squares)   # [1, 4, 9, 16, 25]

# filter() → Filter items
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)   # [2, 4, 6]

# sorted() → Custom sorting
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)   # [('Bob', 20), ('Charlie', 23), ('Alice', 25)]

# reduce()
from functools import reduce

nums = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)
print(product)   # 120