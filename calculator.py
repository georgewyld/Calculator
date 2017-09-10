#CALCULATOR
import math

def addition(a,b):
    c=a+b
    return c

def subtraction(a,b):
    c=a-b
    return c

def division(a,b):
    c=a/b
    return c

def multiplication(a,b):
    c=a*b
    return c

def indicies(a,b):
    c=a**b
    return c

def sqrt(a):
    c=math.sqrt(a)
    return c

def nrt(a,b):
    c=a**(1/b)
    return c




again='yes'

while again=='yes':
    while True:
        try:
            num1=int(input("Please enter the first number: "))
            break
        except ValueError:
            print('Invalid integer')

    while True:
        try:
            num2=int(input("Please enter the second number: "))
            break
        except ValueError:
            print('Invalid integer')
            
    
    operator=input("Please enter your operator ('+','-','*','/','**'): ")
    while True:
        if operator=='+':
            print(addition(num1,num2))
            break
        elif operator=='-':
            print(subtraction(num1,num2))
            break
        elif operator=='*':
            print(multiplication(num1,num2))
            break
        elif operator=='/':
            if num2==0:
                print('You cannot divide by 0')
                num2=int(input("Please re-enter the second number: "))
            print(division(num1,num2))
            break
        elif operator=='**':
            print(indicies(num1,num2))
            break
        elif operator=='sqrt':
            print(sqrt(num1,num2))
            break
        elif operator=='nrt':
            print(nrt(num1,num2))
            break
        
        
        else:
            print("Invalid command")
            operator=input("Please enter your command ('+','-','*','/'): ")
            continue
    again=input("Would you like to enter a new sum (yes/no): ")
    


























