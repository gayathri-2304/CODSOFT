#Calculator

def calc(num1,num2):
    print("1. Addition  2.Subtraction  3.Multiplication  4.Division")
    print("Enter your choice:")
    choice=int(input())
    while(choice>4):
        choice=int(input("Enter correct choice:"))
    if(choice==1):
        print(f"{num1}+{num2}={num1+num2}")
    elif choice==2:
        print(f"{num1}-{num2}={num1-num2}")
    elif choice==3:
        print(f"{num1}*{num2}={num1*num2}")
    elif choice==4:
        if num2==0:
            print("Wrong Num2!!")
            num2=int(input("Enter correct number:"))
        print(f"{num1}/{num2}={num1/num2}")
    
flag=0
while(flag!=1):
    num1=int(input("Enter 1st number:"))
    num2=int(input("Enter 2nd number:"))
    calc(num1,num2)
    print("Do you want to continue or stop?")
    i=int(input("Enter 0 for COntinue and 1 for stop:"))
    if i==1:
        flag=1
    elif i==0:
        flag=0
    while(i>1):
        i=int(input("Enter Valid STatus 0 or 1:"))
        
print("DONE!!!")
        
        
