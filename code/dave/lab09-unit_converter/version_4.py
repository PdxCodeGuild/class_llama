"""
This program will convert the user's input of feet, miles, meter, and kilometers into meters.
"""

# prompt user for distance
distance = input("what is the distance? ")


# prompt user for the unit of measure
input_unit = input("what is the input unit? ie: ft, mi, m, km: ")

# if statement to convert input to meters

if input_unit == "ft":
    value = float(distance) * 0.3048
elif input_unit == "mi":
    value = float(distance) * 1609.344
elif input_unit == "km":
    value = float(distance) * 1000
else:
    value = float(distance) * 1


# if statement to convert meters to output
output_unit = input("what is to output unit? ie: ft, mi, m, km: ")
if output_unit == "ft":
    value = value / 0.3048
    print(distance,input_unit,"is equal to",value,output_unit)
elif output_unit == "mi":
    value = value / 1609.344
    print(distance,input_unit,"is equal to",value,output_unit)
elif output_unit == "km":
    value = value / 1000
    print(distance,input_unit,"is equal to",value,output_unit)
else:
    value = value * 1
    print(distance,input_unit,"is equal to",value,output_unit)