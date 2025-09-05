# Loops


# Basic Loops

# for Loop (when you know how many times to repeat)

# Loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop over a range
for i in range(5):  
    print(i)   # 0,1,2,3,4



# while Loop (when you don’t know the number of repetitions in advance)
count = 1
while count <= 5:
    print(count)
    count += 1


# ___________________________________________________________________________________


# Loop Control Statements

# break → stop the loop completely
for i in range(10):
    if i == 5:
        break
    print(i)
# Output: 0,1,2,3,4



# continue → skip current iteration
for i in range(5):
    if i == 2:
        continue
    print(i)
# Output: 0,1,3,4


# else with Loops (runs only if loop didn’t break)
for i in range(5):
    print(i)
else:
    print("Loop finished!")   # runs if no break


# ________________________________________________________________________________________


# Intermediate Usage

# Nested Loops
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")


# Loop with enumerate()
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
# 0 apple
# 1 banana
# 2 cherry


# Loop with zip()
names = ["Thejas", "Arun", "Ravi"]
scores = [90, 85, 88]

for n, s in zip(names, scores):
    print(f"{n} scored {s}")

# ___________________________________________________________________________________________


# Advanced Loops

#  List Comprehension
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]


# Dictionary Comprehension
nums = [1, 2, 3, 4]
squares = {x: x**2 for x in nums}
print(squares)  # {1:1, 2:4, 3:9, 4:16}


# Generator Expression (efficient looping)
gen = (x**2 for x in range(5))
for val in gen:
    print(val)

