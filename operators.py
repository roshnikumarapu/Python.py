# Task B1.1: Arithmetic Operators

# Declare two integer variables
a = 23
b = 6

# Perform arithmetic operations
print("a + b =", a + b)    # Addition
print("a - b =", a - b)    # Subtraction
print("a * b =", a * b)    # Multiplication
print("a / b =", a / b)    # Division
print("a // b =", a // b)  # Floor Division
print("a % b =", a % b)    # Modulus
print("a ** b =", a ** b)  # Exponent
#output
#a + b = 29
#a - b = 17
#a * b = 138
#a / b = 3.8333333333333335
#a // b = 3
#a % b = 5
#a ** b = 148035889







# Take input from the user
m = int(input("Enter the first integer (m): "))
n = int(input("Enter the second integer (n): "))

# Compare using all six comparison operators
print("m == n :", m == n)   # Equal to
print("m != n :", m != n)   # Not equal to
print("m > n  :", m > n)    # Greater than
print("m < n  :", m < n)    # Less than
print("m >= n :", m >= n)   # Greater than or equal to
print("m <= n :", m <= n)   # Less than or equal to
#output
#m == n : False
#m != n : True
#m > n  : True
#m < n  : False
#m >= n : True
#m <= n : False








# Start with score = 50
score = 50
print("Initial score =", score)

# = (Assignment)
score = 50
print("After '='  :", score)

# += (Addition Assignment)
score += 10
print("After '+=' :", score)

# -= (Subtraction Assignment)
score -= 5
print("After '-=' :", score)

# *= (Multiplication Assignment)
score *= 2
print("After '*=' :", score)

# /= (Division Assignment)
score /= 5
print("After '/=' :", score)

# //= (Floor Division Assignment)
score //= 2
print("After '//=':", score)

# %= (Modulus Assignment)
score %= 3
print("After '%=' :", score)

# **= (Exponent Assignment)
score **= 3
print("After '**=':", score)
#output
#Initial score = 50
#After '='  : 50
#After '+=' : 60
#After '-=' : 55
#After '*=' : 110
#After '/=' : 22.0
#After '//=': 11.0
#After '%=' : 2.0
#After '**=': 8.0








# Take input from the user
percentage = float(input("Enter your percentage: "))
attendance = float(input("Enter your attendance percentage: "))

# Check eligibility
eligible = (percentage > 75) and (attendance > 90)

# Print result
print("Eligible for Scholarship:", eligible)
#output
#Enter your percentage: 82
#Enter your attendance percentage: 95
#Eligible for Scholarship: True








# Declare two integer variables
p = 12
q = 10

# Print binary representations
print("p =", p, "Binary:", bin(p))
print("q =", q, "Binary:", bin(q))

# Perform bitwise operations
print("p & q  =", p & q)      # Bitwise AND
print("p | q  =", p | q)      # Bitwise OR
print("p ^ q  =", p ^ q)      # Bitwise XOR
print("~p     =", ~p)         # Bitwise NOT
print("p << 2 =", p << 2)     # Left Shift
print("p >> 2 =", p >> 2)     # Right Shift
#output
#p = 12 Binary: 0b1100
3q = 10 Binary: 0b1010

#p & q  = 8
#p | q  = 14
#p ^ q  = 6
#~p     = -13
#p << 2 = 48
#p >> 2 = 3









# Create a list of fruits
fruits = ["apple", "banana", "mango", "grape", "kiwi"]

# Take input from the user
item = input("Enter a fruit: ")

# Check membership
print(item, "is in the list:", item in fruits)
print(item, "is not in the list:", item not in fruits)
#output
#Enter a fruit: mango
#mango is in the list: True
#mango is not in the list: False








# Create three lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

# Compare values
print("list1 == list2 :", list1 == list2)   # Same content

# Compare object identity
print("list1 is list2 :", list1 is list2)   # Same object?
print("list1 is list3 :", list1 is list3)   # Same object?

# Using 'is not'
print("list1 is not list2 :", list1 is not list2)
print("list1 is not list3 :", list1 is not list3)

# Print memory addresses
print("ID of list1:", id(list1))
print("ID of list2:", id(list2))
print("ID of list3:", id(list3))
#output
#list1 == list2 : True
#list1 is list2 : False
#list1 is list3 : True
#list1 is not list2 : True
#list1 is not list3 : False
#ID of list1: 140214567890112
#ID of list2: 140214567891456
#ID of list3: 140214567890112






