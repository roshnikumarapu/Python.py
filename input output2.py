name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello", name + ", you will turn", age + 1, "next year.")

# Sample Output:
# Enter your name: Poojitha
# Enter your age: 18
# Hello Poojitha, you will turn 19 next year.


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)
print("Difference =", a - b)
print("Product =", a * b)
print("Quotient =", a / b)

# Sample Output:
# Enter first number: 10
# Enter second number: 5
# Sum = 15
# Difference = 5
# Product = 50
# Quotient = 2.0


name = "Poojitha"
marks = 95

# Comma-separated print()
print("Name:", name, "Marks:", marks)

# str.format()
print("Name: {} Marks: {}".format(name, marks))

# f-string
print(f"Name: {name} Marks: {marks}")

# Output:
# Name: Poojitha Marks: 95
# Name: Poojitha Marks: 95
# Name: Poojitha Marks: 95



nums = input("Enter numbers: ").split()

a = int(nums[0])
b = int(nums[1])
c = int(nums[2])

print("Sum =", a + b + c)

# Sample Output:
# Enter numbers: 10 20 30
# Sum = 60
