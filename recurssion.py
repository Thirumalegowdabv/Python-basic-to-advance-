# Recurssion

# Recursion is when a function calls itself to solve a problem.


# Every recursive function has:

# Base Case → Stops recursion.

# Recursive Case → Function calls itself with smaller input.
    
def countdown(n):
    if n == 0:    # Base Case
        print("Done!")
    else:         # Recursive Case
        print(n)
        countdown(n-1)

countdown(5)
# Output: 5 4 3 2 1 Done!


# Important Notes

# Recursive functions must have a base case, otherwise you’ll get infinite recursion (RecursionError).

# Recursion is powerful but can be slower than loops for large inputs (due to function call overhead).

# Python has a recursion limit (default = 1000). You can check/change it:

# import sys
# print(sys.getrecursionlimit())   # 1000
