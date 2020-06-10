''' 
simple calculator

''' 
# operators = + - / % ** // 

print("welcome to the calculator.")

while True:

    operations = input("select your operations ( + , - , * , /, done):\n")
    num1 = input("what is your first number: ")
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

    elif operations in ["done"]:
        ## will run through numbers before ending
        print("Thank you! Have super day!")
        break
  
   

    print("Answer:" + str(formula))
