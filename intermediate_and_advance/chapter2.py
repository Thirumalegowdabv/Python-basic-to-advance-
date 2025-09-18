# itertools 
# itertools is a standard library in Python for efficient looping.

# It provides tools to handle iterators (objects you can loop over) in memory-efficient and fast ways.

# Great for combinatorics, infinite sequences, grouping, and functional-style programming.


import itertools

# count(start=0, step=1)

# Creates an infinite counter.

for i in itertools.count(10, 2):  # start=10, step=2
    if i > 20:
        break
    print(i)  # 10, 12, 14, 16, 18, 20


# cycle(iterable)

# Repeats the iterable infinitely.

count = 0
for item in itertools.cycle(['A', 'B', 'C']):
    if count > 5:
        break
    print(item)  # A, B, C, A, B, C
    count += 1




# repeat(object, times=None)

# Repeats an object multiple times (or infinitely).

for i in itertools.repeat("Hi", 3):
    print(i)  # Hi, Hi, Hi



# chain(*iterables)

# Links multiple iterables together.

list(itertools.chain([1, 2], ['a', 'b']))
# [1, 2, 'a', 'b']



# compress(data, selectors)

# Filters elements based on a selector list of booleans.

data = 'ABCDEF'
selectors = [1, 0, 1, 0, 1, 0]
print(list(itertools.compress(data, selectors)))
# ['A', 'C', 'E']



#  Filtering & Slicing Iterators
#  islice(iterable, start, stop, step)

# Like slicing but works on iterators.

list(itertools.islice(range(10), 2, 8, 2))
# [2, 4, 6]


# dropwhile(predicate, iterable)

# Skip items while predicate is true, then yield the rest.

list(itertools.dropwhile(lambda x: x < 5, [1,4,6,7,2]))
# [6, 7, 2]



# takewhile(predicate, iterable)

# Take items while predicate is true, then stop.

list(itertools.takewhile(lambda x: x < 5, [1,4,6,7,2]))
# [1, 4]



# filterfalse(predicate, iterable)

# Opposite of filter().

list(itertools.filterfalse(lambda x: x % 2, range(10)))
# [0, 2, 4, 6, 8]



# Grouping & Accumulation
#  groupby(iterable, key=None)

# Groups elements by a key function.

data = [("A", 1), ("A", 2), ("B", 3), ("B", 4)]
for key, group in itertools.groupby(data, lambda x: x[0]):
    print(key, list(group))
# A [('A',1), ('A',2)]
# B [('B',3), ('B',4)]


# accumulate(iterable, func=operator.add)

# Cumulative sum or custom accumulation.

import operator
nums = [1, 2, 3, 4]
print(list(itertools.accumulate(nums)))  
# [1, 3, 6, 10]

print(list(itertools.accumulate(nums, operator.mul)))
# [1, 2, 6, 24]



# Combinatorics Functions
#  product(iterables, repeat=n)

# Cartesian product.

list(itertools.product([1,2], ['a','b']))
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]



# permutations(iterable, r=None)

# All possible orderings.

list(itertools.permutations('ABC', 2))
# [('A','B'), ('A','C'), ('B','A'), ('B','C'), ('C','A'), ('C','B')]



#  combinations(iterable, r)

# Unique combinations (no repeat, order doesn’t matter).

list(itertools.combinations('ABC', 2))
# [('A','B'), ('A','C'), ('B','C')]



# combinations_with_replacement(iterable, r)

# Combinations with repetition allowed.

list(itertools.combinations_with_replacement('ABC', 2))
# [('A','A'), ('A','B'), ('A','C'), ('B','B'), ('B','C'), ('C','C')]



# Advanced Usage Patterns

# Flattening lists

list(itertools.chain.from_iterable([[1,2], [3,4], [5]]))
# [1, 2, 3, 4, 5]



# Creating Infinite Fibonacci with accumulate

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

fib_seq = itertools.islice(fib(), 10)
print(list(fib_seq))  
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# Round-robin Iteration

def round_robin(*iterables):
    return itertools.chain.from_iterable(zip(*iterables))

print(list(round_robin("ABC", "123")))
# ['A','1','B','2','C','3']



# When to Use itertools?

# Efficient looping (no unnecessary lists in memory).

# Combinatorics (permutations, combinations, product).

# Stream processing (takewhile, dropwhile).

# Cumulative calculations (accumulate).

# Data grouping & filtering.


