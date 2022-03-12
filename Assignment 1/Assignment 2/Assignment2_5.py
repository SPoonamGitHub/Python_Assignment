def Prime(n):
          i=2
          j=0
          while i<n:
                    if n%i==0:
                              k=1
                    i=i+1
          return j

x=(int(input("Enter the  number")))
y=Prime(x)
if y==1:
          print(" Prime")
else:
          print("  not Prime")