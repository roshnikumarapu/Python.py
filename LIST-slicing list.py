#A-3
#ex-6

numbers=[12,14,15,16,18,32,54,22,63,48]
print("first three elements:",numbers[:3])
print("last three elements:",numbers[-3:])
print("alternate elements:",numbers[::2])

#output
#first three elements: [12, 14, 15]
#last three elements: [22, 63, 48]
#alternate elements: [12, 15, 18, 54, 63]



#ex-7

numbers=[10,100,1000,10000]
reversed_list=numbers[::-1]
print("original list", numbers)
print("reversed list", reversed_list)

#output
#original list [10, 100, 1000, 10000]
#reversed list [10000, 1000, 100, 10]






#ex-8

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
middle = numbers[4:8]
print("Middle 4 elements:", middle)

#output
#Middle 4 elements: [50, 60, 70, 80]
