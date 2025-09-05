# sets 

# A set is an unordered collection of unique elements in Python.

# It does not allow duplicates.

# It is mutable (can add/remove items), but its elements must be immutable (e.g., numbers, strings, tuples).

# ex 

# Creating a set
my_set = {1, 2, 3, 4}
print(my_set)  # {1, 2, 3, 4}

# Creating from list (duplicates removed)
my_set2 = set([1, 2, 2, 3, 4, 4])
print(my_set2)  # {1, 2, 3, 4}

# _________________________________________________________________________________________________________________________

# Basic Operations

# Add elements
my_set = {1, 2}
my_set.add(3)
print(my_set)  # {1, 2, 3}



# Remove elements
my_set.remove(2)  # Removes 2, Error if not present
my_set.discard(5) # Removes 5, No error if not present
my_set.pop()      # Removes a random element



# Check membership
print(3 in my_set)   # True
print(10 not in my_set)  # True



# Length
print(len(my_set))

# _______________________________________________________________________________


# Set Operations (like Math)

# Union (A ∪ B)
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)         # {1, 2, 3, 4, 5}
print(A.union(B))    # {1, 2, 3, 4, 5}



# Intersection (A ∩ B)
print(A & B)             # {3}
print(A.intersection(B)) # {3}



# Difference (A − B)
print(A - B)             # {1, 2}
print(A.difference(B))   # {1, 2}



# Symmetric Difference (A △ B)
print(A ^ B)                  # {1, 2, 4, 5}
print(A.symmetric_difference(B))

# _________________________________________________________________________


# Set Methods (Important)

A = {1, 2, 3}
B = {2, 3}

print(A.issubset(B))      # False
print(B.issubset(A))      # True

print(A.issuperset(B))    # True
print(A.isdisjoint(B))    # False


# _____________________________________________________________________________________


# Frozenset (Immutable Set)

# Normal sets are mutable, but frozenset is immutable.

# Useful when you need sets as dictionary keys.

fs = frozenset([1, 2, 3])
print(fs)        # frozenset({1, 2, 3})

# fs.add(4) ❌ Error (immutable)

# _________________________________________________________________

# Advanced Usage

# Set Comprehension
squares = {x**2 for x in range(5)}
print(squares)  # {0, 1, 4, 9, 16}



# Removing duplicates from a list
nums = [1, 2, 2, 3, 4, 4]
unique_nums = list(set(nums))
print(unique_nums)  # [1, 2, 3, 4] (order not guaranteed)



# Intersection of multiple sets
A = {1, 2, 3, 4}
B = {2, 3, 5}
C = {3, 6}

print(A & B & C)   # {3}



# Frozen sets in dictionary
d = {frozenset([1,2]): "value"}
print(d)  # {frozenset({1, 2}): 'value'}

# .........................................................................




