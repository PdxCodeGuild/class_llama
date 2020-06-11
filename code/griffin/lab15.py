def number_finder(num,dict):
    for n in dict:
        if n == num:
            word_number = dict.get(n)
            return word_number


def main():
    number = int(input("enter a number between 1 and 999: ")) #gets the number to be evaluated
    
    #sets tens and hundreds place words as a blank space by default for numbers < 10, <100
    hundreds_place_word = ""
    tens_place_word = ""
    
    #all the dictionaries showing how to convert
    hundreds_words = {0:"",1:"one hundred-",2:"two hundred-",3:"three hundred-",4:"four hundred-",5:"five hundred-",6:"six hundred-",7:"seven hundred-",8:"eight hundred-",9:"nine hundred-"}
    tens_words = {0:"", 2:"twenty-", 3:"thirty-", 4:"forty-", 5:"fifty-", 6:"sixty-", 7:"seventy-", 8:"eighty-", 9:"ninety-"}
    ones_words = {0:"", 1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    teen_exceptions = {10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}

    #isolates each digit
    hundreds_digit = number//100
    teen_exception = number%100
    tens_digit = (number%100)//10
    ones_digit = number%10

    #looks through the dictionaries for each digit and finds the appropriate words
    hundreds_word = number_finder(hundreds_digit,hundreds_words)

    if tens_digit == 1:
        tens_and_ones = number_finder(teen_exception,teen_exceptions)
                
    else:            
        tens_place_word = number_finder(tens_digit,tens_words)
        ones_place_word = number_finder(ones_digit, ones_words)
        tens_and_ones = f"{tens_place_word}{ones_place_word}"
    
    print(f"{hundreds_word}{tens_and_ones}")



if __name__ == "__main__":
    main()