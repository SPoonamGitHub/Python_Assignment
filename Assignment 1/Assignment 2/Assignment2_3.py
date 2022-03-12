def factorial(n):
  i=1
  while n>0:
     i=n*i
     n=n-1
   
  return i
   
x=(int(input("enter the number:")))
print("factorial is:",x,factorial(x)) 