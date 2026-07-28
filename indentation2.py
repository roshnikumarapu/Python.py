x = 10

if x > 0:
print("Positive")
else:
    print("Negative")

# Error:
# IndentationError: expected an indented block after 'if' statement

x = 10

if x > 0:
    print("Positive")
else:
    print("Negative")

# Output:
# Positive


for i in range(1, 11):
    if i % 2 == 0:
        print(i, "Even")
    else:
        print(i, "Odd")

# Output:
# 1 Odd
# 2 Even
# 3 Odd
# 4 Even
# 5 Odd
# 6 Even
# 7 Odd
# 8 Even
# 9 Odd
# 10 Even

x = int(input("Enter a number: "))

if x > 0:
    print("Positive")
else:
    print("Non-positive")

# Sample Output:
# Enter a number: -5
# Non-positive




