name = "Poojitha"
age = 18
height = 5.4
student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(student, type(student))

# Output:
# Poojitha <class 'str'>
# 18 <class 'int'>
# 5.4 <class 'float'>
# True <class 'bool'>



# Assign different values in one line
a, b, c = 10, 20, 30
print(a, b, c)

# Assign same value in one line
a = b = c = 100
print(a, b, c)

# Output:
# 10 20 30
# 100 100 100



a = 10
b = 20

temp = a
a = b
b = temp

print("a =", a)
print("b =", b)

# Output:
# a = 20
# b = 10


a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)

# Output:
# a = 20
# b = 10


x = 100
print(x)
print(type(x))

x = "Python"
print(x)
print(type(x))

# Output:
# 100
# <class 'int'>
# Python
# <class 'str'>

