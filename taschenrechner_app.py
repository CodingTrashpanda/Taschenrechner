from typing import Union


def add(a:int, b:int)->int:
    return a+b

def sub(a:int, b:int)->int:
    return a-b
    
def mul(a:int, b:int)->int:
    return a*b

def div(a:int, b:int)-> Union[int,float,None]:
    try:
        return a/b
    except ZeroDivisionError:
        return None

def log_result(function, a, b):
    result = function(a, b)
    if result != None:
        res = f"{a} {function.__name__} {b} = {result}\n"
        print(res)
        with open("result.txt", "a") as f:
            f.write(res)
    else:
        if function == div:
            print("division by zero is not allowed")

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "A" or choice == "a":
        print("Addition")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        log_result(add, a, b)
    elif choice == "B" or choice == "b":
        print("Subtraction")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        log_result(sub, a, b)
    elif choice == "C" or choice == "c":
        print("Multiplication")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        log_result(mul, a, b)
    elif choice == "D" or choice == "d":
        print("Division")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        log_result(div, a, b)
    elif choice == "E" or choice == "e":
        print("Program Ended")
        quit()
