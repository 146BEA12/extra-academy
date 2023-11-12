import math
def add(a, b):
    c = a + b
    print("a + b = ", c)

def subtract(a, b):
    c = a - b
    print("a - b = ", c)

def multiply(a, b):
    c = a * b
    print("a * b = ", c)

def divide(a, b):
    c = a / b
    print("a / b = ", c)

def sqr_root(a):
    print("Square root of ",a ,"is", math.sqrt(a))

statement = True
while statement:
    print(" ")
    print("Available options: ")
    print("1. a + b")
    print("2. a - b")
    print("3. a * b")
    print("4. a / b")
    print("5.Find square root")
    print("6. EXIT")

    choice = input("Enter option: ")

    if choice.isdigit():
        if choice == "1":
            a = int(input("Enter first digit a: "))
            b = int(input("Enter second digit b: "))
            add(a, b)

        elif choice == "2":
            a = int(input("Enter first digit a: "))
            b = int(input("Enter second digit b: "))
            subtract(a, b)

        elif choice == "3":
            a = int(input("Enter first digit a: "))
            b = int(input("Enter second digit b: "))
            multiply(a, b)

        elif choice == "4":
            a = int(input("Enter first digit a: "))
            b = int(input("Enter second digit b: "))
            divide(a, b)

        elif choice == "5":
            a = int(input("Enter digit: "))
            sqr_root(a)
        
        else:
            statement = False
    
    else:
        print(" ")
        print("You entered a string, enter a integer to continue using the calculator.") 