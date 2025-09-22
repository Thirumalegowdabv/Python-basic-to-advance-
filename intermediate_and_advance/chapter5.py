# Python has a built-in module called random for generating random numbers.

# 1.Importing the Module
import random

# 2. Generating Random Integers
import random

# Random integer between 1 and 10 (inclusive)
print(random.randint(1, 10))


# randint(a, b) gives an integer between a and b, inclusive.


# 3.Random Floating-Point Numbers
# Random float between 0.0 and 1.0
print(random.random())

# Random float between 1.5 and 5.5
print(random.uniform(1.5, 5.5))



# 4.Random Choice from a List
fruits = ["apple", "banana", "cherry", "mango"]

print(random.choice(fruits))  # picks one element randomly



# 5. Multiple Random Choices
# Pick 2 random items from the list (with replacement)
print(random.choices(fruits, k=2))

# Pick 2 random items (without replacement, unique values)
print(random.sample(fruits, 2))



# 6. Shuffling a List
deck = [1, 2, 3, 4, 5]
random.shuffle(deck)
print(deck)  # order changes randomly




# 7. Seeding Random Numbers

# If you want reproducible results (same random output every time), use seed():

random.seed(42)
print(random.randint(1, 100))  # always same number with same seed



# 8. Advanced Random (with NumPy)

# For data science & machine learning, we often use NumPy’s random module:

# import numpy as np

# # Random array of integers
# print(np.random.randint(1, 10, size=5))

# # Random floats between 0 and 1
# print(np.random.rand(3))



# Summary

# random.randint(a, b) → random integer

# random.random() → random float (0 to 1)

# random.uniform(a, b) → random float in range

# random.choice(list) → pick one item

# random.sample(list, k) → pick multiple unique items

# random.shuffle(list) → shuffle list

