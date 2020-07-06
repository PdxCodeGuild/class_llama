"""1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
1 yard is 0.9144 m
1 inch is 0.0254 m"""

unit = input("\nIs the thing measured in inches, feet, yards, miles, meters, or kilometers? ")
length = float(input(f"\nHow long is the thing in {unit}? "))
new_unit = (input("\nWould you like that converted to inches, feet, yards, miles, meters, or kilometers? "))

if unit == "feet":
    meters = .3048 * length
elif unit == "inches":
    meters = .0254 * length
elif unit == "miles":
    meters = 1609.34 * length
elif unit == "meters":
    meters = length
elif unit == "kilometers":
    meters = length / 1000
elif unit == "yards":
    meters = .9144 * length

conversion_table = {"feet":.3048, "inches":.0254,"miles":1609.34,"meters":1,"kilometers":.001,"yards":.9144}
for x in conversion_table:
    if x == new_unit:
       operator = conversion_table.get(x)
       

output = meters/operator
print(f"\nthat thing is {output} {new_unit} long")