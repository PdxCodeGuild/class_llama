# Unit Converter 
 
# ft = 0.3048
# mi = 1609.34
# km = 1000

print("Feet/Mile/Kilometer Unit Converter Program!")

num1 = int(input("Enter numbers for the distance in Meters: "))
choice_2 = input("Enter ft/mi/km: ")

if choice_2 == "ft":
    output = int(num1)*3.28084
    print(num1, "meters", "*", 3.28084, "feet", "=", (num1 * 3.28084) )
elif choice_2 == "mi":
    output = int(num1)*1609.34
    print(num1, "meters", "*", 1609.34, "miles", "=", (num1 * 1609.34) )
elif choice_2 == "km":
    output = input(num1)*1000
    print(num1, "meters", "*", 1000, "kilometers", "=", (num1 * 1000) )
else:
    print("")  