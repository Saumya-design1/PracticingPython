# CALCULATOR
# This is a simple calculator program that performs basic arithmetic operations.

# Take user input for two numbers and the desired operation, then perform the calculation and display the result.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

op = input("Enter the operation (+, -, *, /): ")

if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    result = num1 / num2

print("Result:", result)