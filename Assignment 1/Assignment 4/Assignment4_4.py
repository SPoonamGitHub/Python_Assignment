from functools import reduce

check=lambda no:  no%2==0

Increment=lambda no: no**2

Addition=lambda a,b :a+b

def main():
 
 data=[int(x) for x in (input("enter the values")).split()]
 print ("original data:", data)

 newdata = list(filter(check,data))
 print("data after filter:", newdata)
 
 Incrementdata=list(map(Increment,newdata))
 print("data after map:",Incrementdata)
 
 ret=reduce(Addition,Incrementdata)
 print("data after reduce:", ret)

if __name__=="__main__":
 main()