#Simple Calculator

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b!=0:
        return a/b
    else:
        print("Error:Division by zero!")
        
print("Simple Calculator")
print("-----------------")
while True:
    print("Operations:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    
    choice=input("Enter your choice from(1-5): ")
    if choice=="5":
        print("Calculator program has ended.")
        break
    n1=int(input("Enter the first number:"))
    n2=int(input("Enter the second number:"))
    
    if choice=="1":
        result=add(n1,n2)
        print("Result:",result)
    elif choice=="2":
        result=subtract(n1,n2)
        print("Result:",result)
    elif choice=="3":
        result=multiply(n1,n2)
        print("Result:",result)
    elif choice=="4":
        result=divide(n1,n2)
        print("Result:",result)
    else:
        print("Invlaid choice.Please enter a number between 1 and 5.")        
