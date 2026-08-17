#ex-8
n = int(input("Enter N: "))

i = 1
while i <= n:
    print(i)
    i += 1
    
#output
#Enter N: 5
#1
#2
#3
#4
#5





#ex-9
n = int(input("Enter a number: "))

temp = n
sum = 0
count = 0

while temp > 0:
    digit = temp % 10
    sum += digit
    count += 1
    temp //= 10

average = sum / count

print("Sum =", sum)
print("Average =", average)

#output
#Enter a number: 44
#Sum = 8
#Average = 4.0




#ex-10
n = int(input("Enter a number: "))

reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reverse =", reverse)

#output
#Enter a number: 34567
#Reverse = 76543




#ex-11
n=(int(input("enter a number")))
reverse=0
original=n
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n = n // 10
if original==reverse:
    print("palindrome")
else:
    print("not a palindrome")

#output
#enter a number34543
#palindrome







#ex-12
n = int(input("Enter N: "))
a = 0
b = 1
i = 1

while i <= n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    i += 1

#output
#Enter N: 9
#0 1 1 2 3 5 8 13 21 




