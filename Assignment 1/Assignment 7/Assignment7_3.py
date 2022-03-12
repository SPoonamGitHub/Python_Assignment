
def DisplayR(i=5):
                 
  if(i>0):
   print(i,end=" ")
   i=i-1
   DisplayR(i)  #Recursive call
 

def main():
 DisplayR()

if __name__=="__main__":
 main()