import threading

def evenfactor(num):
 sum=0
 for i in range(1,num):
  if num%i==0 and i%2==0:
   sum=sum+i
   print("even :",sum)

def oddfactor(num):
 sum=0
 for i in range(1,num):
  if num%i==0 and i%2!=0:
   sum=sum+i
   print("odd :",sum)
   
if __name__=="__main__":   
 num=int(input("enter number"))
 
 thread1=threading.Thread(target=evenfactor, args=(num,))
 thread2=threading.Thread(target=oddfactor, args=(num,))

 thread1.start()
 thread2.start()

 thread1.join()
 thread2.join()
 print(" exit fom main.")