# Docstrings

# Docstring (Documentation String) is a string literal that appears right after the definition of a function, class, or module.
# It is used to explain what the code does.

# Enclosed in triple quotes (""" """ or ''' ''').

# Can be multi-line or single-line.

# Accessible via .__doc__.


def add(a, b):
    """
    This function takes two numbers and returns their sum.
    
    Parameters:
        a (int or float): First number
        b (int or float): Second number
    
    Returns:
        int or float: Sum of a and b
    """
    return a + b

print(add.__doc__)

# output 
# This function takes two numbers and returns their sum.

# Parameters:
#     a (int or float): First number
#     b (int or float): Second number

# Returns:
#     int or float: Sum of a and b



# Why write docstrings ?

# Readability & Maintainability

# Imagine coming back to your own code after 6 months — docstrings help you quickly recall what the function does.

# Team Projects / Professional Work

# When you work in companies or open-source projects, other developers need to understand your code.

# Well-written docstrings save time and avoid confusion.

# Documentation Tools

# Libraries like NumPy, Pandas, Django use docstrings.

# Tools like pydoc or Sphinx can generate full documentation websites automatically from docstrings.

# Interview / Good Practices

# In interviews, writing clean code with docstrings shows professionalism.
