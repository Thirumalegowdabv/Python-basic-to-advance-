#  here we learn about control statements 

# if Statement

# Used to check a condition.

# If the condition is True, the block inside if runs.

# example 
# x = 10
# if x > 5:
#     print("x is greater than 5") , output = x is greater than 5

# _____________________________________

# elif (else if)

# Used when you want to check multiple conditions.

# It comes after an if.

# Only the first true condition will execute, then Python stops checking further.

# example 
x = 10
if x > 15:
    print("x is greater than 15")
elif x == 10:
    print("x is exactly 10")
elif x > 5:
    print("x is greater than 5")     #output = x is exactly 10

# ______________________________________________________________________


# else

# Runs when none of the if or elif conditions are true.

# example
x = 3
if x > 10:
    print("x is greater than 10")
elif x == 5:
    print("x is 5")
else:
    print("x is less than or equal to 5 and not 5")  #output = x is less than or equal to 5 and not 5

# _______________________________________________________________

# all combine 

marks = 72

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")   #output = Grade C

# __________________________________________

# Remember:

# You can have only one if.

# You can have multiple elifs.

# You can have at most one else, and it must be last.
