"""
This program will convert the user's input of feet, miles, meter, and kilometers into meters.
"""

# prompt user for distance
distance = input("what is the distance? ")

# prompt user for the unit of measure
unit = input("what are the units? ie: inch, yard, ft, mi, m, km: ")

# if statement to run correct equation for conversion based on user input
if unit == "ft":
    ft_to_meters = float(distance) * 0.3048
    print(distance,"ft is",round(ft_to_meters, 4),"m")
elif unit == "mi":
    mi_to_meters = float(distance) * 1609.344
    print(distance,"mi is",round(mi_to_meters, 4),"m")
elif unit == "km":
    km_to_meters = float(distance) * 1000
    print(distance,"km is",round(km_to_meters, 4),"m")
elif unit == "yard":
    yard_to_meters = float(distance) * 0.9144
    print(distance,"yard is",round(yard_to_meters, 4),"m")
elif unit == "inch":
    inch_to_meters = float(distance) * 0.0254
    print(distance,"inch is",round(inch_to_meters, 4),"m")
else:
    print(distance,"m is already in meters.")