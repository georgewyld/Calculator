#calculator 2.0
import math, operator, sys


operators={
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow,
    'sqrt': math.sqrt,
    'quit': sys.exit,
}

def main():
    while True:
        
        func = operators.get(input("Please choose an operator\n(+,-,*,/,**,sqrt,quit): "), None)
        if func is None:
            print("Invalid operator!")
            continue
        elif func == math.sqrt:
            print(func(float(input('Please enter the number you would like to square root: '))))
        elif func==sys.exit:
            break
        else:
            while True:
                try:
                    num1=float(input('Please enter the first number: '))
                    break
                except ValueError:
                    print('Invalid Number')
            while True:
                try:
                    num2=float(input('Please enter the second number: '))
                    break
                except ValueError:
                    print('Invalid Number')
            print('Answer = ',func(num1,num2))
                    
                    


name='main'
if name=='main':
    print("Welcome to the python calculator")
    main()
    






































