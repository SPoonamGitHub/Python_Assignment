def printPattern(n):
          for i in range(n):
                    j=i+1
                    while j<=n:
                              print("*",end=" ")
                              j+=1
                    print("\n")

x=(int(input("Enter the number")))
printPattern(x)