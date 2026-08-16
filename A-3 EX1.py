 #ex-1
a=(int(input("enter a value")))
if a>0:
    print("a is positive")
elif a<0:
    print("a is positive")
else:
    print("a is zero")
#output    
#enter a value0
#a is zero




#ex-2
a=(int(input("enter a year")))
if a%4==0:
    print("a is leap year")
else:
    print("a is not a leap year")
#output
#enter a year2014
#a is not a leap year



#ex-3
a=(int(input("enter side1:")))
b=(int(input("enter side2:")))
c=(int(input("enter side3:")))
if a==b==c:
    print("equilateral triangle")
elif a==b or b==c or c==a:
    print("isosceles triangle")
elif a!=b!=c:
    print("scalene triangle")
else:
    print("not a valid triangle")
#output
#enter side1:3
#enter side2:4
#enter side3:5
#scalene triangle




#ex-4
a=(int(input("enter a value")))
b=(int(input("enter b value")))
c=(int(input("enter c value")))
if a>b or a>c:
    print("a is greater")
else:
    if b>a or b>c:
        print("b is greater")
    else:
        if c>a or c>b:
            print("c is greater")
#output
#enter a value3
#enter b value5
#enter c value4
#b is greater



#ex-5
b=(int(input("enter student marks")))
if b>=95:
    print("A grade")
elif b>=75:
    print("B grade")
elif b>=60:
    print("C grade")
elif b>=40:
    print("D grade")
else:
    print("FAIL")
    
#output
#enter student marks78
#B grade



#ex-6
ch = input("Enter a character: ")

if ch in "aeiouAEIOU":
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
elif ch.isdigit():
    print("Digit")
else:
    print("Special symbol")

#output
#Enter a character: u
#Vowel



#ex-7
year =int(input("Enter year: "))
month =int(input("Enter month: "))
day = int(input("Enter day: "))

if month < 1 or month > 12:
    print("Invalid date")

elif month == 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        if day >= 1 and day <= 29:
            print("Valid date")
        else:
            print("Invalid date")
    else:
        if day >= 1 and day <= 28:
            print("Valid date")
        else:
            print("Invalid date")

elif month in [4, 6, 9, 11]:
    if day >= 1 and day <= 30:
        print("Valid date")
    else:
        print("Invalid date")

else:
    if day >= 1 and day <= 31:
        print("Valid date")
    else:
        print("Invalid date")

#output
#Enter year: 2028
#Enter month: 3
#Enter day: 24
#Valid date




        
            
         
           

    


