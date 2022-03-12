import Arithmetic as A

def main():
 print("inside module:",__name__)
 no1=int(input("enter first number:"))
 no2=int(input("enter second number:"))
 
 ret=A.Add(no1,no2)
 print("Addition is :", ret)
 
 ret=A.Sub(no1,no2)
 print("subtraction is :", ret)
 
 ret=A.Mul(no1,no2)
 print("Multiplication is :", ret)
 
 ret=A.Div(no1,no2)
 print("Division is :", ret)




if __name__=="__main__":
 main()
