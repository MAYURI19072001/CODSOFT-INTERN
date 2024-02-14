def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if a!=0:
        return a/b
    else:
        return "error: cannot divide by zero."

def calculator():
    print("simple calculator")
    print("operation")
    print("add")
    print("sub")
    print("multiply")
    print("divide")
    
num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
operation=input("select operation(add/sub/multiply/divide):")

if operation == "add":
    result = add (num1,num2)
elif operation == "sub":
    result = sub (num1 ,num2)
elif operation == "multiply":
     result= multiply (num1 ,num2)
elif operation == "divide":
    result= divide(num1,num2)
else:
    result="error: invalid operation."
    
print(f"result:{result}") 
