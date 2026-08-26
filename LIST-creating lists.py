#week-4
#A-1
#1

numbers=[10,20,30,40,50,60,70,80,90,100]
print("list:",numbers)
print("length:",len(numbers))

#output
#list: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#length: 10




#2
my_list=[10,32.34,"hello",True,[1,2,3]]

for element in my_list:
    print(element,"->",type(element))

#output
#10 -> <class 'int'>
#32.34 -> <class 'float'>
#hello -> <class 'str'>
#True -> <class 'bool'>
#[1, 2, 3] -> <class 'list'>






#3
my_list=[]
my_list.append(10)
my_list.append(12)
my_list.append(7)
my_list.append(45)
my_list.append(18)
print("the list is",my_list)

#output
#the list is [10, 12, 7, 45, 18]


