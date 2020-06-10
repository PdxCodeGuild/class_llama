''' 
simple calculator

''' 
# operators = + - / % ** // 

comp = input("welcome to the calculator.")

while True:

    num1 = input("what is your first number: ")
    operations = input("select your operations ( + , - , * , /):\n")
    num2 = input("what is your second number: ")

    num1 = float(num1)
    num2 = float(num2)

    formula = None

    if operations == "+":
        formula = num1 + num2

    elif operations == "-":
        formula = num1 - num2

    elif operations == "*":
        formula = num1 * num2

    elif operations == "/":
        formula = num1 / num2

    if num1 = "done":
        break

    print("Answer:" + str(formula))
