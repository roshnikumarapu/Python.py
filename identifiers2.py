#1.
# Variable
name = "Pooja"

# Constant-style name
MAX = 100

# Function name
def show():
    return "Hello"

# Class name
class Student:
    pass

# Identifier with underscore
my_name = "Python"

# Print all identifiers
print(name)
print(MAX)
print(show())
print(Student)
print(my_name)

#output: Pooja
#100
#Hello
#<class '__main__.Student'>
#Python


#2,
# 2value  -> Invalid (starts with a number)

value_2 = 10
print("value_2 is a valid identifier")

_hidden = 20
print("_hidden is a valid identifier")

# class -> Invalid (Python keyword)

# my-var -> Invalid (contains '-')

MyClass = "Python"
print("MyClass is a valid identifier")

# total$ -> Invalid (contains '$')

#output: value_2 is a valid identifier
#_hidden is a valid identifier
#MyClass is a valid identifier


#3.# Python is case-sensitive

Marks = 90
marks = 75

print("Marks =", Marks)
print("marks =", marks)

#output: Marks = 90
#marks = 75 
