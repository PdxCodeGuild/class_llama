def number_finder(num,dict):
    for n in dict:
        if n == num:
            numeral = dict.get(n)
            return numeral


def main():
    number = int(input("enter a number between 1 and 999: ")) #gets the number to be evaluated
    
    #sets tens and hundreds place words as a blank space by default for numbers < 10, <100
    hundreds_numeral = ""
    tens_numeral = ""
    
    #all the dictionaries showing how to convert
    hundreds_numerals = {0:"",1:"C",2:"CC",3:"CCC",4:"CD",5:"D",6:"DC",7:"DCC",8:"DCCC",9:"CM"}
    tens_numerals = {0:"", 1:"X",2:"XX", 3:"XXX", 4:"XL", 5:"L", 6:"LX", 7:"LXX", 8:"LXXX", 9:"XC"}
    ones_numerals = {0:"", 1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX"}
    
    #isolates each digit
    hundreds_digit = number//100
    tens_digit = (number%100)//10
    ones_digit = number%10

    #looks through the dictionaries for each digit and finds the appropriate words
    hundreds_numeral = number_finder(hundreds_digit,hundreds_numerals)   
    tens_numeral = number_finder(tens_digit,tens_numerals)
    ones_numeral = number_finder(ones_digit, ones_numerals)
    
    
    print(f"{hundreds_numeral}{tens_numeral}{ones_numeral}")



if __name__ == "__main__":
    main()