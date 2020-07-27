print("Welcome to the Distance Converter!")
user_input = int(input("What is the distance?: "))
user_input1 = input("What is the input unit of measurement?")
user_input2 = input("What is the output unit of measurement?")

if user_input1 == "ft" and user_input2 == "m":
    print(user_input * .3048 )
if user_input1 == "ft" and user_input2 == "mi":
    print(user_input / 5280 )
if user_input1 == "ft" and user_input2 == "km":
    print(user_input / 3280 )
if user_input1 == "m" and user_input2 == "ft":
    print(user_input / .3048 )
if user_input1 == "m" and user_input2 == "mi":
    print(user_input / 1609.34  )
if user_input1 == "m" and user_input2 == "km":
    print(user_input / 1000 )
if user_input1 == "mi" and user_input2 == "ft":
    print(user_input * 5280 )
if user_input1 == "mi" and user_input2 == "m":
    print(user_input * 1609 )
if user_input1 == "mi" and user_input2 == "km":
    print(user_input / 1.609 )
if user_input1 == "km" and user_input2 == "m":
    print(user_input * 1000 )
if user_input1 == "km" and user_input2 == "ft":
    print(user_input / 3280.84 )
if user_input1 == "km" and user_input2 == "mi":
    print(user_input * .621371 )

