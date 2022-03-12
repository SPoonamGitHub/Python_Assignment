def DisplayR(no):
 if (no>0):
  print("*" ,end=" ")
  no=no-1
  DisplayR(no)  #Recursive call
 

def main():
 DisplayR(5)

if __name__=="__main__":
 main()