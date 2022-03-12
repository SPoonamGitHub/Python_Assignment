from functools import reduce
def is_prime(num):
   for j in range(2, num):
      if num % j == 0:
         return False
   else:
      return True

def main():
 
 data=[int(x) for x in (input("enter the values")).split()]
 print ("original data:", data)

 newdata = list(filter(is_prime,data))
 print("data after filter:", newdata)
 
 Incrementdata=list(map(lambda no:no*2,newdata))
 print("data after map:",Incrementdata)
 
 ret=reduce(lambda x,y: x if x > y else y,Incrementdata)
 print("data after reduce:", ret)

if __name__=="__main__":
 main()	  
	  