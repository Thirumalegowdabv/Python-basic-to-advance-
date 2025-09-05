# built in functions

# print(abs(-5.5)) , abs returns the absolute value example it returns only non negative numbers, regardless of its sign

# print(round(6.3)) , here round function round of the vlaue to the nearest integer

# ____________________________________________________________________________________________________________________


# enums are the readable names which are bound to constants values
# to use this enums we need import it from standard enum libraray

# from enum import Enum

# class Student(Enum):
#     BEST = 0
#     AVERAGE = 1
    
# print(Student.BEST.value)   , output = 0
# print(Student["BEST"].value) , output = 0
# print(Student(1))   , output = Student.AVERAGE
# print(list(Student))    it lists the  values of the Student 


# _____________________________________________________________________________________________


# user inputs 
# here we learn about how can a user can give inputs manually that is inside a program and outside a porgram(compilation)

#  it can be implemented by using user input() function

# print("what is your age?")
# age=input()                , in this line we give input in the terminal 
# print("your age is :" + age) , here we get the output like your age is 30

# other way 

# age=input("what is your age?")        
# print("your age is :" + age)   ,   same output but here inorder to get the output we need enter our age first then we will get your age is 30


# ______________________________________________________________________________

# Basics of Functions

# Defining a Function

def greet():
    print("Hello, World!")

greet()  # Hello, World!



# Function with Parameters

def add(a, b):
    return a + b

print(add(5, 3))  # 8



# Default Arguments

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Thejas")   # Hello, Thejas!
greet()           # Hello, Guest!


# ________________________________________________________________________________________

# Intermediate Function Features

# Keyword Arguments

def student(name, age):
    print(f"Name: {name}, Age: {age}")

student(age=20, name="Thejas")




# Variable Arguments

# *args → multiple positional arguments
def total(*nums):
    return sum(nums)

print(total(1, 2, 3, 4))  # 10

# **kwargs → multiple keyword arguments
def show_info(**data):
    for k, v in data.items():
        print(f"{k}: {v}")

show_info(name="Thejas", age=20, lang="Python")


# Returning Multiple Values

def math_ops(a, b):
    return a+b, a-b, a*b

add, sub, mul = math_ops(5, 2)
print(add, sub, mul)  # 7 3 10


# ___________________________________________________________________


# Advanced Function Concepts

# Anonymous Functions (Lambda)
square = lambda x: x**2
print(square(4))  # 16




# Map, Filter, Reduce

nums = [1, 2, 3, 4]

# map
squares = list(map(lambda x: x**2, nums))   # [1, 4, 9, 16]

# filter
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]

# reduce
from functools import reduce
product = reduce(lambda x, y: x*y, nums)   # 24



# Recursion (Function calling itself)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # 120



# Closures

def outer(x):
    def inner(y):
        return x + y
    return inner

add5 = outer(5)
print(add5(10))   # 15



# Decorators

def decorator(func):
    def wrapper():
        print("Before call")
        func()
        print("After call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
# Before call
# Hello!
# After call


