# Unit Converter

def conversion():
    
    num = input("Enter the distance in numerical value: ")
    unit = input("Enter the unit you would like to use [in, ft, yd, m, mi, km]: ")

    if unit == "in":
        in_num = float(num) * 0.0254
        print(f"{num} in is {in_num} m!")

    elif unit == "ft":
        ft_num = float(num) * 0.3048
        print(f"{num} ft is {ft_num} m!")

    elif unit == "yd":
        yd_num = float(num) * 0.9144
        print(f"{num} ft is {yd_num} m!")
    
    elif unit == "m":
        m_num = float(num) * 1
        print(f"{num} m is {m_num} m!")

    elif unit == "mi":
        mi_num = float(num) * 1609.34
        print(f"{num} m is {mi_num} m!")

    elif unit == "km":
        km_num = float(num) * 1000
        print(f"{num} m is {km_num} m!")

    else:
        print("Sorry, that was not a valid input.")



def main():
    print("We are going to do some conversion!")
    conversion()


main()