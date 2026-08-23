
#ex-18
N = int(input("Enter number of rows: "))

for i in range(1, N + 1):
    for j in range(i):
        print("*", end="")
    print()

#output   
#Enter number of rows: 5
#*
#**
#***
#****
#*****






#ex-19
N = int(input("Enter number of rows: "))
for i in range(N, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

#output
#Enter number of rows: 5
#*****
#****
#***
#**
#*






#ex-20
N = int(input("Enter number of rows: "))

for i in range(1, N + 1):
    for j in range(N - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

#output
#Enter number of rows: 5
 #   *
   #***
#  *****
# *******
#*********







#ex-21
N = int(input("Enter number of rows: "))

for i in range(N, 0, -1):
     Print spaces
    for j in range(N - i):
        print(" ", end="")

     Print stars
    for j in range(2 * i - 1):
        print("*", end="")

    print()

#output
#Enter number of rows: 5
#*********
 #*******
 # *****
  # ***
   # *







#ex-22
N = int(input("Enter number of rows: "))

# Upper half
for i in range(1, N + 1):
    for j in range(N - i):
        print(" ", end="")
    
    for j in range(2 * i - 1):
        print("*", end="")
    
    print()

# Lower half
for i in range(N - 1, 0, -1):
    for j in range(N - i):
        print(" ", end="")
    
    for j in range(2 * i - 1):
        print("*", end="")
    
    print()

#output



    
