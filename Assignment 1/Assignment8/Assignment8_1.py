import threading
 
number=20
def even():
 for i in range(1,number+1):
  if i%2==0:
   print("even number:",i)

def odd():
 for i in range(1,number+1):
  if i%2!=0:
   print("odd number :",i)
  
 
if __name__=="__main__":

 thread1=threading.Thread(target=even , args=())
 thread2=threading.Thread(target=odd ,args=())
 
 thread1.start()
 thread1.join()
 thread2.start()
 
 
 thread2.join()