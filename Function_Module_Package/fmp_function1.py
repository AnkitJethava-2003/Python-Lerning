import sys
import os
num1=10
num2=20

def add(num1, num2):
    result=num1+num2
    print(result)

def sub(num1, num2):
    result=num1-num2
    print(result)

def multi(num1, num2):
    result=num1*num2
    print(result)

def div(num1, num2):
    result=num1/num2
    print(result)

num1= float (sys.argv[1])
operation=sys.argv[2]
num2=float (sys.argv[3])

if operation == "add":
    output=add(num1, num2)
    print(output)

print(os.getenv("password"))