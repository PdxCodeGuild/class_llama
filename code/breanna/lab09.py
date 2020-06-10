# Unit Converter

def conversion():
    num = input("Enter the distance in feet: ")
    c_num = float(num) * 0.3048
    print(f"{num} feet is {c_num} meters!")

def main():
    print("We are going to do some conversion!")
    conversion()


main()