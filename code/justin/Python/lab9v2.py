# Version 2 & 3

count = 0
while count < 1:
    print("I'm the meter converter! I convert lots of things to meters -- like feet, miles, kilometers, inches, yards, even meters!")
    unit = input("What unit do you want to convert to meters?: ").lower()
    num_units = int(input("How many of those do you want converted to meters? Please type a numerical value: "))

    feet = num_units * 0.3048
    miles = num_units * 1609.34
    kilometers = num_units * 1000
    inches = num_units * 0.9144
    yards = num_units * 0.0254

    if unit == "feet" or "foot" or "ft":
        print(f"{num_units} ft is {feet} m!")

    elif unit == "miles" or "mile" or "mi":
        print(f"{num_units} mi is {miles} m!")

    elif unit == "kilometers" or "kilometer" or "km":
        print(f"{num_units} km is {kilometers} m!")

    elif unit == "meters" or "meter" or "m":
        print(f"{num_units} m is {num_units} m, but you already knew that.")

    elif unit == "yards" or "yard" or "yd":
        print(f"{num_units} mi is {yards} yd!")

    elif unit == "inches" or "inch" or "in":
        print(f"{num_units} km is {inches} in!")

    more = input("Would you like to convert more?: ").lower()
    if more == "yes":
        pass
    if more == "no":
        print("Suit yourself.")
        count += 1





