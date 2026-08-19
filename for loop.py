#ex-13
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)

#output
#Enter a number: 7
#7 x 1 = 7
#7 x 2 = 14
#7 x 3 = 21
#7 x 4 = 28
#7 x 5 = 35
#7 x 6 = 42
#7 x 7 = 49
#7 x 8 = 56
#7 x 9 = 63
#7 x 10 = 70






#ex-14
n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)

#output
#Enter a number: 7
#Factorial = 5040






#ex-15
s = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0

for ch in s:
    if ch in "aeiouAEIOU":
        vowels += 1
    elif ch.isalpha():
       consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1

print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Spaces =", spaces)

#output
#Enter a string: ewus3
#Vowels = 2
#Consonants = 2
#Digits = 1
#Spaces = 0






#ex-16
n = int(input("Enter a number: "))

if n < 2:
    print("Not Prime")
else:
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print("Prime")
    else:
        print("Not Prime")

#output
#Enter a number: 45
#Not Prime










#ex-17
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for n in range(start, end + 1):
    if n < 2:
        continue

    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print(n, end=" ")
#output
#Enter starting number: 10
#Enter ending number: 30
#11 13 17 19 23 29



