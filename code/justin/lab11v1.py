# Lab 11, Calculator
# Version 1

print("Welcome to the Calculator!")

# Number Inputs
num1 = int(input("First number?: "))
num2 = int(input("Second number?: "))

# Operation Functions
def add(num1, num2):
    '''This function will add two inputted numbers'''
    added = num1 + num2
    return added
def subtract(num1, num2):
    '''This function will subtract two inputted numbers'''
    subtracted = num1 - num2
    return subtracted
def divide(num1, num2):
    '''This function will divide two inputted numbers'''
    if num2 != 0:
        divided = num1 / num2
        return divided
def multiply(num1, num2):
    '''This function will multiply two inputted numbers'''
    multiplied = num1 * num2
    return multiplied

# Returned Variables
added = add(num1, num2)
subtracted = subtract(num1, num2)
divided = divide(num1, num2)
multiplied = multiply(num1, num2)

#Operation Input Loop
while True:    
    operation = str.lower(input("What operation would you like?: "))
    if operation == "add" or "+":
        print(f"{num1} + {num2} = {added}")
        break
    elif operation == "subtract" or "-":
        print(f"{num1} - {num2} = {subtracted}")
        break
    elif operation == "multiply" or "*" or "x":
        print(f"{num1} * {num2} = {multiplied}")
        break
    elif operation == "divide" or "/":
        print(f"{num1} / {num2} = {divided}")
        break
    else:
        print("I don't understand.")
