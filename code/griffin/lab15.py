
def main():
    number = int(input("enter a number between 1 and 99: "))
    tens_place_word = ""
    tens_words = {0:"", 2:"twenty-", 3:"thirty-", 4:"forty-", 5:"fifty-", 6:"sixty-", 7:"seventy-", 8:"eighty-", 9:"ninety-"}
    ones_words = {0:"", 1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    teen_exceptions = {10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}

    tens_digit = number//10
    ones_digit = number%10
    if number > 19 or number < 10:
        for n in tens_words:
            if n == tens_digit:
                tens_place_word = tens_words.get(n)


        for n in ones_words:
            if n == ones_digit:
                ones_place_word = ones_words.get(n)
        print(f"{tens_place_word}{ones_place_word}")
    else:
        for n in teen_exceptions:
            if n == number:
                teen_word = teen_exceptions.get(n)
                print(teen_word)

    




if __name__ == "__main__":
    main()