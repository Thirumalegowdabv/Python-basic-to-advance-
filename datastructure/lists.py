# List 
# A list in Python is a collection of ordered, changeable (mutable), and indexed elements.

# It can hold different data types (integers, strings, floats, even other lists).

# Lists are written inside square brackets [].

fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40]
mixed = [25, "hello", 3.14, True]

# _________________________________________________________________________________________________

# Accessing List Elements

# Lists are indexed starting from 0.

fruits = ["apple", "banana", "cherry"]

print(fruits[0])   # first element → apple
print(fruits[1])   # second element → banana
print(fruits[-1])  # last element → cherry

# _________________________________________________________________________________________________

# Changing List Elements

# Lists are mutable, so you can update values.

fruits = ["apple", "banana", "cherry"]
fruits[1] = "mango"
print(fruits)   # ['apple', 'mango', 'cherry']

# _________________________________________________________________________________________________

# List Operations

# Length

print(len(fruits))   # 3



# Add elements

fruits.append("orange")      # adds at end
fruits.insert(1, "grapes")   # adds at index 1



# Remove elements

fruits.remove("apple")  # removes by value
fruits.pop(2)           # removes by index
del fruits[0]           # delete first element



# Slicing

numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[2:])    # [30, 40, 50]



# Iterating Over Lists

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)     #output = apple banana cherry



# Useful List Functions

numbers = [5, 2, 9, 1, 7]

print(max(numbers))   # 9
print(min(numbers))   # 1
print(sum(numbers))   # 24

numbers.sort()        # sort ascending
print(numbers)        # [1, 2, 5, 7, 9]

numbers.reverse()     # reverse order
print(numbers)        # [9, 7, 5, 2, 1]



# _________________________________________________________________________________________________

# In short:

# List = container that can store multiple values.

# Mutable = you can change, add, and remove items.

# Indexed = access by position.


# .............................................................................................................



# List compressions

# A concise way to create lists.
# Instead of writing a loop, you can build lists in one line.

# Syntax:
# [expression for item in iterable if condition]

#  Basic Example

# Without list comprehension:

squares = []
for i in range(5):
    squares.append(i * i)
print(squares)

# With list comprehension:

squares = [i * i for i in range(5)]
print(squares)  # [0, 1, 4, 9, 16]



# With Condition

# You can add if to filter elements.

evens = [i for i in range(10) if i % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]




#  Nested Loops

# You can use more than one loop.

pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(pairs)  # [(1, 3), (1, 4), (2, 3), (2, 4)]




# With Functions

# You can apply functions directly.

words = ["hello", "python", "world"]
uppercased = [w.upper() for w in words]
print(uppercased)  # ['HELLO', 'PYTHON', 'WORLD']




# List Comprehension with if-else

# You can use a conditional expression.

nums = [1, 2, 3, 4, 5]
labels = ["even" if n % 2 == 0 else "odd" for n in nums]
print(labels)  # ['odd', 'even', 'odd', 'even', 'odd']




# Nested List Comprehension

# Flattening a matrix:

matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6]



# Advantages

# Short and readable
# Faster than normal loops in many cases
# Powerful for transformations + filtering

