def Add(x):
          i=1
          sum=0
          while x>i:
                    if x%i==0:
                              sum=sum+i
                    i=i+1
          return sum

x=(int(input("Enter the  number")))
print("Sum is",+Add(x)) 