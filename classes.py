# Classes

# A class is a blueprint for creating objects.
# An object is an instance of a class (real-world entity).

# Defining a class
class Dog:
    pass

# Creating objects
dog1 = Dog()
dog2 = Dog()

print(type(dog1))  # <class '__main__.Dog'>




# Attributes (Variables inside a class)

# Class Attributes → Shared by all objects.

# Instance Attributes → Unique to each object.

class Dog:
    species = "Canine"   # class attribute
    
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age

dog1 = Dog("Tommy", 5)
dog2 = Dog("Sheru", 3)

print(dog1.name, dog1.age)   # Tommy 5
print(dog2.name, dog2.age)   # Sheru 3
print(dog1.species)          # Canine



# Methods (Functions inside a class)

# Instance Method → Works with object data.

# Class Method → Works with class data (@classmethod).

# Static Method → Utility method, not dependent on class/object (@staticmethod).

class Dog:
    species = "Canine"
    
    def __init__(self, name):
        self.name = name
    
    # Instance Method
    def bark(self):
        return f"{self.name} is barking!"
    
    # Class Method
    @classmethod
    def info(cls):
        return f"All dogs are {cls.species}"
    
    # Static Method
    @staticmethod
    def sound():
        return "Dogs say Woof!"

d = Dog("Tommy")
print(d.bark())       # Tommy is barking!
print(Dog.info())     # All dogs are Canine
print(Dog.sound())    # Dogs say Woof!






