"""
This program will be a simple REPL calculator for addition, subtraction,
multiplication, and division. It will prompt user to enter the operation
and convert it to an int and generate the answer. 
"""

# create a function for each operation: add, sub, mult, div

# add
def add(num1, num2):
    total = num1 + num2
    return total

# sub
def sub(num1, num2):
    total = num1 - num2
    return total

# mult
def mult(num1, num2):
    total = num1 * num2
    return total

# div
def div(num1, num2):
    total = num1 / num2
    return total

# prompt user to enter the operation they want
operator = input("what is the operation you'd like to perform?: ")

# prompt user to enter 2 numbers
num1 = float(input("what is the first number?: "))
num2 = float(input("what is the second number?: "))

# if statement that selects correct math function to apply to input numbers
if operator == "+":
    value = add(num1,num2)
    print(num1,operator,num2,"=", value)
elif operator == "-":
    value = sub(num1,num2)
    print(num1,operator,num2,"=", value)
elif operator == "*":
    value = mult(num1,num2)
    print(num1,operator,num2,"=", value)
elif operator == "/":
    value = div(num1,num2)
    print(num1,operator,num2,"=", value)
else:
    print("You did not enter a valid input")