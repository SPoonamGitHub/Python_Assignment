
list=[]
num=int(input("total elemen in list"))

for i in range(num):
 element=int(input("enter the number"))
 list.append(element)
 
print("frequency of number", format(list.count(element) ))
 