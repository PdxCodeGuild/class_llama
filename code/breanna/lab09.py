# Unit Converter

def conversion_m():
    
    num = input("Enter the distance in numerical value: ")
    input_unit = input("Enter the input unit [in, ft, yd, m, mi, km]: ")
    output_unit = input("Enter the output unit [in, ft, yd, m, mi, km]: ")

    # convert to meters
    if input_unit == "in":
        num_m = float(num) * 0.0254

    elif input_unit == "ft":
        num_m = float(num) * 0.3048

    elif input_unit == "yd":
        num_m = float(num) * 0.914

    elif input_unit == "m":
        num_m = float(num) * 1

    elif input_unit == "mi":
        num_m = float(num) * 1609.34

    elif input_unit == "km":
        num_m = float(num) * 1000


    # full conversion
    if output_unit == "in":

        print(f"{num} {input_unit} is {num_m/0.0254} {output_unit}!")

    elif output_unit == "ft":

        print(f"{num} {input_unit} is {num_m/0.3048} {output_unit}!")

    elif output_unit == "yd":

        print(f"{num} {input_unit} is {num_m/0.914} {output_unit}!")
    
    elif output_unit == "m":

        print(f"{num} {input_unit} is {num_m/1.0} {output_unit}!")

    elif output_unit == "mi":

        print(f"{num} {input_unit} is {num_m/1609.34} {output_unit}!")

    elif output_unit == "km":

        print(f"{num} {input_unit} is {num_m/1000.0} {output_unit}!")

    else:
        print("Sorry, that was not a valid input.")


def main():
    print("We are going to do some conversion!")
    conversion_m()


main()
