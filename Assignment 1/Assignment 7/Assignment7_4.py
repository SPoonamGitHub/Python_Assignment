def Display(n):
 sum=0
 while(n>0):
  sum = sum + n % 10
  n = n / 10
  print("sum")
  Display(sum)

def main():
 Display(sum)


if __name__=="__main__":
 main()