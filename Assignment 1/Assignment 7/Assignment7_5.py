def factorial(n=5):
  i=1
  while(n>0):
    i=n*i
    print(i)
    n=n-1
	  
    factorial(i)
  
def main():
 factorial()
 

if __name__=="__main__":
 main() 
   
