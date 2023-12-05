n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
print("1.addition\n 2.substraction\n 3.multiplication\n 4.division\n")
ch=int(input("enter your choice:"))
if ch==1:
    sum=n1+n2
    print("sum of two number:",sum)
elif ch==2:
    sum=n1-n2
    print("difrence of two number:",sum)
elif ch==3:
    sum=n1*n2
    print("product of two numbers:",sum)
elif ch==4:
    sum=n1/n2
    print("quotient of two number:",sum)
else:
    print("enter correct choice!!")
    
       
