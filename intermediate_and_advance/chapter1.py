# What is collections?
# collections is a built-in Python module that provides specialized container datatypes beyond the basic list, tuple, dict, and set.
# It makes working with data easier, especially when counting, grouping, or organizing data.


# Key Classes in collections
# a) Counter
   # A dict subclass for counting hashable items.
   # Very useful for frequency analysis.
   
from collections import Counter

data = "aaabbc"
count = Counter(data)
print(count)  # Counter({'a': 3, 'b': 2, 'c': 1})

print(count.most_common(1))  # [('a', 3)]
print(count['b'])             # 2



# b) namedtuple

  # A lightweight object type similar to a class.
  # Creates tuples with named fields, making code more readable.

from collections import namedtuple

Point = namedtuple('Point', 'x y')
p = Point(10, -5)
print(p.x, p.y)  # 10 -5



# c) deque

    # A double-ended queue. Fast append and pop operations from both ends.
    # Useful for implementing queues, stacks, or sliding windows.

# Example:

from collections import deque

dq = deque([1, 2, 3])
dq.append(4)       # Add to right
dq.appendleft(0)   # Add to left
print(dq)          # deque([0, 1, 2, 3, 4])

dq.pop()           # Remove from right -> 4
dq.popleft()       # Remove from left -> 0


# Advanced usage:

dq.rotate(2)       # Rotate right by 2 -> deque([2, 3, 1])




# d) defaultdict

    # A dict subclass that provides a default value for missing keys.
    # Saves you from KeyError.

# Example:

from collections import defaultdict

dd = defaultdict(int)  # Default value is 0
dd['a'] += 1
dd['b'] += 2
print(dd)  # defaultdict(<class 'int'>, {'a': 1, 'b': 2})


# Advanced usage:

# Using list as default
dd = defaultdict(list)
dd['fruits'].append('apple')
print(dd)  # defaultdict(<class 'list'>, {'fruits': ['apple']})




# e) OrderedDict (Python 3.7+ preserves insertion order in normal dict, but OrderedDict has extra methods)

    # Keeps items in insertion order.
    # Useful for reordering, popping first/last item.

# Example:

from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
print(od)  # OrderedDict([('a', 1), ('b', 2)])

# Pop first item
od.popitem(last=False)
print(od)  # OrderedDict([('b', 2)])





# f) ChainMap

    # Groups multiple dictionaries into a single view.
    # Useful for managing multiple scopes, like configs or defaults.

# Example:

from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

cm = ChainMap(dict1, dict2)
print(cm['b'])  # 2 -> first dict takes priority
print(cm['c'])  # 4




# g) UserDict, UserList, UserString

    # Base classes for custom dict, list, string subclasses.
    # Useful when you want to override or extend behavior.

# Example:

from collections import UserDict

class MyDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value*2)  # Double the value

md = MyDict()
md['a'] = 5
print(md)  # {'a': 10}





#                            Summary Table
# Class	                                                     Use Case

# Counter                                   	Count elements, most common items
# namedtuple	                                Lightweight class-like tuples
# deque	                                        Efficient queues and stacks
# defaultdict       	                        Dict with default values for missing keys
# OrderedDict       	                        Dict that remembers insertion order
# ChainMap	                                    Combine multiple dicts
# UserDict/UserList/UserString	                Custom dict/list/string behavior



#  Tips / Advanced Tricks

# Combine Counter and most_common to find top N elements in a list/string.

# Use deque for sliding window problems.

# Use defaultdict(list) to group data by key.

# Use namedtuple + _replace for immutable updates.

# ChainMap is great for layered configs or environment variables.
