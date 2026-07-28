import sys

name = sys.argv[1]
print("Hello,", name + "!")

# Run:
# python greet.py Alice

# Output:
# Hello, Alice!


import sys

if len(sys.argv) != 3:
    print("Please enter exactly 2 numbers.")
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print("Sum =", a + b)

# Run:
# python add.py 10 20

# Output:
# Sum = 30


import sys

print("Script Name:", sys.argv[0])
print("Total Arguments:", len(sys.argv))

# Run:
# python test.py 10 20

# Output:
# Script Name: test.py
# Total Arguments: 3



