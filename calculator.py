import math

print("Hello There!!! miss me😎")
print("Am here. Lets calculate💲🤑")
# addition
def add(a, b):
    return a + b
#subtraction
def subtract(a, b):
    return a - b
#multiplication
def multiply(a, b):
    return a * b
#exponential
def exponent(a, b):
    return a ** b
#squareroot
def sqrt(a):
    return math.sqrt(a)
#square
def square(a):
    return a**2
#division
def divide(a, b):
    if b == 0:
        return "cannot divide by zero"
    return a / b
print("select operator: ")
print("+. addition")
print("-. subtraction")
print("*. multiplication")
print("/. division")
print("^. square")
print("**. exponent")
print("|. squareroot")


while True:
    choice = input("Enter an operator: ")

    if choice == "+":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = add(num1, num2)
        print(result)
    elif choice == "-":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = subtract(num1, num2)
        print(result)
    elif choice == "*":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = multiply(num1, num2)
        print(result)
    elif choice == "/":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = divide(num1, num2)
        print(result)
    elif choice == "^":
        num1 = float(input("Enter a number: "))
        result = square(num1)
        print(result)
    elif choice == "**":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = exponent(num1, num2)
        print(result)
    elif choice == "|":
        num1 = float(input("Enter a number: "))
        result = sqrt(num1)
        print(result)

    else:
        print("invalid operator!!! use operators listed above")
        continue
    next = input("Do you want to continue? (y/n): ")
    if next.lower() == "y":
        continue
    else:
        print("Adios!!")
        break

