"""
This program will convert the user's input of feet into meters.
"""

# prompt user for distance in feet
distance_in_feet = input("What is the distance in feet? ")
print(distance_in_feet)

# convert user's input from feet to meters
distance_in_meters = float(distance_in_feet) * 0.3048
print(distance_in_feet,"ft is",round(distance_in_meters, 4),"m")