# Dictionaries
# A dictionary is a collection of key-value pairs.

# Keys = identifiers (must be unique and immutable like strings, numbers, or tuples).

# Values = can be anything (string, int, list, dict, etc.).

student = {
    "name": "Thejas",
    "age": 21,
    "course": "CSE"
}
print(student) #output = {'name': 'Thejas', 'age': 21, 'course': 'CSE'}


# __________________________________________________________

# Creating Dictionaries

# Method 1 – using {}
my_dict = {"a": 1, "b": 2, "c": 3}

# Method 2 – using dict() function
my_dict2 = dict(a=1, b=2, c=3)

# Method 3 – from list of tuples
pairs = [("x", 10), ("y", 20)]
my_dict3 = dict(pairs)

print(my_dict3)  # {'x': 10, 'y': 20}

# __________________________________________________________________

# Accessing Elements

student = {"name": "Thejas", "age": 21}

print(student["name"])    # Thejas
print(student.get("age")) # 21
print(student.get("marks", "Not Found"))  # Safe access → Not Found

# _________________________________________________________

# Adding and Updating

student["age"] = 22          # update
student["college"] = "XYZ"   # add new key
print(student)

# __________________________________________________________

# Removing Items

student.pop("age")      # removes key "age"
del student["college"]  # delete "college"
student.clear()         # empty dictionary

# ___________________________________________________

# Looping Through Dictionary

person = {"name": "Alice", "age": 25, "city": "Bangalore"}

# Keys
for k in person:
    print(k)

# Values
for v in person.values():
    print(v)

# Key + Value
for k, v in person.items():
    print(k, ":", v)

# ___________________________________________________________

# Dictionary Methods

person = {"name": "Alice", "age": 25}

print(person.keys())      # dict_keys(['name', 'age'])
print(person.values())    # dict_values(['Alice', 25])
print(person.items())     # dict_items([('name','Alice'), ('age',25)])

# Update / Merge
person.update({"age": 26, "country": "India"})
print(person)

# ________________________________________________________________

# Dictionary Comprehension

# You can create dictionaries in one line like lists.

squares = {x: x*x for x in range(5)}
print(squares)   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# With condition:

even_squares = {x: x*x for x in range(10) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# ________________________________________________________________

# Nested Dictionaries

# Dictionaries inside dictionaries.

students = {
    "s1": {"name": "Thejas", "age": 21},
    "s2": {"name": "Anu", "age": 22}
}

print(students["s1"]["name"])  # Thejas

# ________________________________________________________________

# Advanced Dictionary Tools

# Python has a module collections with special dictionary types.


# a) defaultdict

# Automatically provides default values.

from collections import defaultdict

marks = defaultdict(int)  # default = 0
marks["math"] += 10
print(marks["science"])   # 0 (no error, default value returned)



# b) OrderedDict

# Maintains insertion order (before Python 3.7). Now normal dict does this.

from collections import OrderedDict
od = OrderedDict()
od["a"] = 1
od["b"] = 2
print(od)


# c) Counter

# Counts frequencies.

from collections import Counter
text = "banana"
count = Counter(text)
print(count)   # Counter({'a': 3, 'n': 2, 'b': 1})


# d) ChainMap

# Combines multiple dictionaries.

from collections import ChainMap
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
cm = ChainMap(d1, d2)
print(cm["b"])  # 2 (takes from first dict)

# ________________________________________________________________


# Real-Life Example

inventory = {
    "laptop": {"brand": "Dell", "price": 55000, "stock": 10},
    "phone": {"brand": "Samsung", "price": 20000, "stock": 25}
}

# Print stock of laptops
print(inventory["laptop"]["stock"])  # 10

# Update stock
inventory["laptop"]["stock"] -= 2
print(inventory["laptop"]["stock"])  # 8




