list=[]
num=int(input("total number in list"))

for i in range(num):
 element=int(input("enter element"))
 list.append(element)
 
print("largest element is",max(list))