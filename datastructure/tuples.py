#  Tuples

# A tuple is a collection of items like a list,

# BUT unlike lists, tuples are immutable → you cannot change, add, or remove elements after creation.

# Tuples are written inside parentheses ().

fruits = ("apple", "banana", "cherry")
numbers = (10, 20, 30, 40)
mixed = (25, "hello", 3.14, True)


# _________________________________________________________

# Properties of Tuples

# Ordered → items have a fixed position.

# Immutable → once created, cannot be modified.

# Allow duplicates → same values can appear multiple times.

example = (1, 2, 2, 3, 4)
print(example)   # (1, 2, 2, 3, 4)

# _________________________________________________________

# Accessing Tuple Elements

# Tuples are indexed just like lists.

fruits = ("apple", "banana", "cherry")

print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[-1])  # cherry

# ___________________________________________________________

# Tuple with One Element

# ⚠️ To create a tuple with one item, add a comma , after it.

single = ("apple",)
print(type(single))   # <class 'tuple'>

not_tuple = ("apple")
print(type(not_tuple)) # <class 'str'>

# ______________________________________________________________

# Tuple Operations

# Length

print(len(fruits))   # 3

# ___________________________________________________________

# Concatenation

t1 = (1, 2, 3)
t2 = (4, 5)
print(t1 + t2)   # (1, 2, 3, 4, 5)

# ___________________________________________________________

# Repetition

print(t1 * 2)   # (1, 2, 3, 1, 2, 3)

# _____________________________________________________________

# Slicing

numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])   # (20, 30, 40)
print(numbers[:3])    # (10, 20, 30)
print(numbers[2:])    # (30, 40, 50)

# _________________________________________________________________

# Iterating Over Tuples

fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit) 
    
# Output:

# apple
# banana
# cherry

# _________________________________________________________________

# Tuple Functions

numbers = (5, 2, 9, 1, 7)

print(max(numbers))   # 9
print(min(numbers))   # 1
print(sum(numbers))   # 24
print(numbers.count(2)) # 1 → counts how many times 2 appears
print(numbers.index(9)) # 2 → index of first occurrence of 9

# ____________________________________________________________________

# When to Use a Tuple?

# Use a list when you need to modify data.

# Use a tuple when data should stay constant (e.g., coordinates, fixed settings, days of the week).

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
