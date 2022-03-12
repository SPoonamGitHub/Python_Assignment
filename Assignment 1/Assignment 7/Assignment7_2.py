
def DisplayR(i=1):
                  
  if(i<6):
   print(i,end=" ")
   i=i+1
   DisplayR(i)  #Recursive call
 

def main():
 DisplayR()

if __name__=="__main__":
 main()