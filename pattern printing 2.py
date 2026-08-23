#ex-23
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(i, end="")
    print()

#output    
#1
#22
#333
#4444
#55555







#ex-24
n = 5

num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

#output
#1 
#2 3 
#4 5 6 
#7 8 9 10 
#11 12 13 14 15





#ex-25
n = 5

for i in range(1, n + 1):
    # Increasing numbers
    for j in range(1, i + 1):
        print(j, end=" ")

    # Decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()

#output1 
#1 2 1 
#1 2 3 2 1 
#1 2 3 4 3 2 1 
#1 2 3 4 5 4 3 2 1







#ex-26
n = 5

for i in range(n):
    for j in range(i + 1):
        print(chr(65 + i), end=" ")
    print()

#output
#A
#B B
#C C C
#D D D D
#E E E E E












#ex-27
n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#output
#* * * * *
#*       *
#*       *
#*       *
#* * * * *











#ex-28
n = 4

# Upper half
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")

# Lower half
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")
#output
 #  *
 # * *
 #*   *
#*     *
# *   *
 # * *
 #  *












#ex-29
n = 5
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

#output
#1
#2 3
#4 5 6
#7 8 9 10
#11 12 13 14 15













#ex-30
n = 4

# Upper half
for i in range(1, n + 1):
    print("* " * i, end="")
    print("  " * (2 * (n - i)), end="")
    print("* " * i)

# Lower half
for i in range(n - 1, 0, -1):
    print("* " * i, end="")
    print("  " * (2 * (n - i)), end="")
    print("* " * i)
        
#output
#*       *
#* *     * *
#* * *   * * *
#* * * * * * * *
#* * *   * * *
#* *     * *
#*       *
