# Version 4

meters_in_units = {
    'ft': 0.3048,
    'mi': 1609.34,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254,
    'm': 1
}

def to_meters(length, input_units):
    return length * meters_in_units[input_units]

def from_meters(old_length):
    return old_length / meters_in_units[final_units]

def standard_units(input_units):
    if input_units in ['feet', 'foot', 'ft']:
        return 'ft'
    elif input_units in ['miles', 'mile', 'mi']:
        return 'mi'
    elif input_units in ['kilometers', 'kilometer', 'km']:
        return 'km'
    elif input_units in ['yards', 'yard', 'yd']:
        return 'yd'
    elif input_units in ['inches', 'inch', 'in']:
        return 'in'
    elif input_units in ['meters', 'meter', 'm']:
        return 'm'


print("Welcome to the unit converter!")

length = float(input("What's the numbered distance you want to convert?: "))
input_units = standard_units(input("That distance is in what units?: "))
final_units = standard_units(input("What do you want that converted to?: "))

old_length = to_meters(length, input_units)
new_length = from_meters(old_length)

print(f"{length} {standard_units(input_units)} is {new_length} {standard_units(final_units)}!")




