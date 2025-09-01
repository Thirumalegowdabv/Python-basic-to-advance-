#operators

#assignment operator 
#ex a = 20 , here "=" symbol used to assign value of 20 to a so this "=" used as assignment operator

#arithmatic operator = "+","-","*","/","%","**","//"
# 1+1 = 2
# 2-2 = 0
# 2*2 = 4
# 2/2 = 1
# 4%3 = 1
# 4**2 = 16 (** = it is a exponent operator)
# 5//2 = 2  (// = it devides the integer and returns quotient by discarding remainder)

# these airthmatic operators can be used with assignment operators
# ex a=10 
# a+=9  , here a= a+9 where the final output = 19  

# _______________________________________________________________________

#comparrison operators = "==","!=" , ">=" , "<=" ,"<" ,">"
#are udsed to compare the vlaues 
#ex a=9 , b=10
# a==b ,false
# a!=b ,true
# a<b  ,true
# a>b  ,false
# a<=b ,true
# a>=b ,true

# ____________________________________________________________________________


# boolean operators = true or false 
# boolean are used during conditional checking for example if the condition true ,it says true and if not it says ,  false 
# ex 
# a =10
# if(a==10):   #  output : thoja
# if (a==0):   #  output : good boi 
#    print("thoja")   
# else:
#     print("good boi") 
    
    
# conditional operators = "not" , "and" , "or"

#ex
#operator  expression              result
# and      true and true           true
#          true and false          false
# or       false and false         false
#          true and false          true
# not      not true , not false    ture  

# ___________________________________________________________________________

#bitwise operators = "&" , "||" , "^" , "`" , "<<" , "<<"
# "&" (bitwise AND ) 
#ex
# a = 6   # 110 (in binary)
# b = 3   # 011

# print(a & b)   # 2  (010 in binary)


# "||"(bitwise OR)
#ex 
# a = 6   # 110
# b = 3   # 011

# print(a | b)   # 7  (111 in binary)



# "^" (bitwise XOR)
#a = 6   # 110
# b = 3   # 011

# print(a ^ b)   # 5  (101 in binary)


# "`" (bitwise NOT)
#ex
# a = 6   # 110
# print(~a)   # -7


# "<<"(shiftf left)
#ex
# a = 6   # 110
# print(a << 1)   # 12 (1100)
# print(a << 2)   # 24 (11000)


# ">>"(shift right)
#ex
# a = 6   # 110
# print(a >> 1)   # 3 (011)
# print(a >> 2)   # 1 (001)

# __________________________________________________________

#is and in operators 

#is operator(identity operator) checks if two variables point to the same object in memory
#it not compares values , but object
#ex
# a = [1, 2, 3]
# b = a          # b refers to the same list
# c = [1, 2, 3]  # a new list with same values

# print(a is b)   # True  (same object in memory)
# print(a is c)   # False (different objects, even though values same)
# print(a == c)   # True  (because values are equal)





#in operator(membership operator) checks a value exists inside a sequence
#returns true if found , otherwise false
#exception "in" operator in dictionary checks the keys , not values
#ex 
# nums = [10, 20, 30, 40]
# print(20 in nums)      # True
# print(50 in nums)      # False
# print(50 not in nums)  # True

# _____________________________________________________________________________________

#ternary operator(also called conditional expression) lets you to write an i_else statement in a single line 
#syntax  value_if_true if condition else value_if_false

#ex 
# x = 10
# result = "Even" if x % 2 == 0 else "Odd"
# print(result)   # Output: Even
