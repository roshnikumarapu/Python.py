import keyword

# Print total number of keywords
print("Total keywords:", len(keyword.kwlist))

# Print the list of keywords
print("Keywords:")
print(keyword.kwlist)

# Output (Python 3.12)
# Total keywords: 35
# Keywords:
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async',
# 'await', 'break', 'class', 'continue', 'def', 'del',
# 'elif', 'else', 'except', 'finally', 'for', 'from',
# 'global', 'if', 'import', 'in', 'is', 'lambda',
# 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
# 'try', 'while', 'with', 'yield']


import keyword

word = input("Enter a word: ")

if keyword.iskeyword(word):
    print(word, "is a Python keyword")
else:
    print(word, "is not a Python keyword")

# Sample Output:
# Enter a word: for
# for is a Python keyword

# Enter a word: hello
# hello is not a Python keyword


for = 5
True = 10

# Error:
# SyntaxError: invalid syntax
