def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

# Input from the user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()

operation = input("Enter the operation (+, -, *, /): ")

# Perform the calculation based on the user's choice
if operation == "+":
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = subtract(num1, num2)
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = multiply(num1, num2)
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    result = divide(num1, num2)
    print(f"{num1} / {num2} = {result}")
else:
    print("Invalid operation. Please enter +, -, *, or /.")