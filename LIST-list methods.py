#A-5
#ex-11
numbers=[5,1,6,9,2,3,0,1]
print("original list:",numbers)
numbers.append(6)
print("after append(6):",numbers)
numbers.insert(4,12)
print("after insertion:",numbers)
numbers.extend([11,4])
print("after extend:",numbers)
numbers.remove(1)
print("after removing 1:",numbers)
numbers.pop()
print("after popping:",numbers)
numbers.sort()
print("after sorting:",numbers)
numbers.reverse()
print("after reversing:",numbers)
count = numbers.count(5)
print("Count of 5:", count)
print("List after count():", numbers)
index = numbers.index(5)
print("Index of 5:", index)
print("List after index():", numbers)

#output
#original list: [5, 1, 6, 9, 2, 3, 0, 1]
#after append(6): [5, 1, 6, 9, 2, 3, 0, 1, 6]
#after insertion: [5, 1, 6, 9, 12, 2, 3, 0, 1, 6]
#after extend: [5, 1, 6, 9, 12, 2, 3, 0, 1, 6, 11, 4]
#after removing 1: [5, 6, 9, 12, 2, 3, 0, 1, 6, 11, 4]
#after popping: [5, 6, 9, 12, 2, 3, 0, 1, 6, 11]
#after sorting: [0, 1, 2, 3, 5, 6, 6, 9, 11, 12]
#after reversing: [12, 11, 9, 6, 6, 5, 3, 2, 1, 0]
#Count of 5: 1
#List after count(): [12, 11, 9, 6, 6, 5, 3, 2, 1, 0]
#Index of 5: 5
#List after index(): [12, 11, 9, 6, 6, 5, 3, 2, 1, 0]





#ex-12
numbers = [1, 2, 3, 2, 4, 1, 5, 3]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print("Original list:", numbers)
print("List after removing duplicates:", unique)

#output
#Original list: [1, 2, 3, 2, 4, 1, 5, 3]
#List after removing duplicates: [1, 2, 3, 4, 5]








#ex-13
numbers = [10, 25, 5, 40, 15]
maximum = numbers[0]
minimum = numbers[0]
total = 0
for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

    total = total + num
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Sum:", total)

#output
#Maximum: 40
#Minimum: 5
#Sum: 95





#ex-14
list1 = [1,2,3,4]
list2 = [5,6,7,8]
combine=list1 + list2
print("list after combining:",combine)
combine=combine[::-1]
print("list after reversing:",combine)
#output
#list after combining: [1, 2, 3, 4, 5, 6, 7, 8]
#list after reversing: [8, 7, 6, 5, 4, 3, 2, 1]
