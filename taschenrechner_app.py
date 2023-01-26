def add (a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")
    with open("result.txt", "a") as f:
        f.write(f"{a} + {b} = {answer}\n")

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")
    with open("result.txt", "a") as f:
        f.write(f"{a} - {b} = {answer}\n")
    
def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")
    with open("result.txt", "a") as f:
        f.write(f"{a} * {b} = {answer}\n")
    
def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")
    with open("result.txt", "a") as f:
        f.write(f"{a} / {b} = {answer}\n")
    
    
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
        add(a, b)
    elif choice == "B" or choice == "b":
        print("Subtraction")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        sub(a, b)
    elif choice == "C" or choice == "c":
        print("Multiplication")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        mul(a, b)
    elif choice == "D" or choice == "d":
        print("Division")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        div(a, b)
    elif choice == "E" or choice == "e":
        print("Program Ended")
        quit()
