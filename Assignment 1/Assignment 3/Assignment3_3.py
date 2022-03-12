list=[]
num=int(input("total number in list"))

for i in range(num):
 element=int(input("enter number"))
 list.append(element)
 
print("samllest element",min(list)) 