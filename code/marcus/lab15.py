
# Courtesy of Taro Ogawa, enhanced by Marius Grigaitis, and 

# from num2words import num2words

# choice = input('Pick a number: ')

# print(num2words(choice))


num = int(input("Pick a number: "))


def numberconverter(num):
    #create a dictionary where the key is a number and the value is a string
    number_dict = {1: "one" , 2: "two" , 3: "three" , 4: "four" , 5: "5" , 
    6: "6" , 7: "seven" , 8: "eight" , 9: "nine" , 10: "ten" , 11: "eleven" , 12: "twelve" ,  
    13: "thirteen" , 14: "fourteen" , 15: "fifteen" , 16: "sixteen" , 17: "seventeen" , 18: "eighteen" , 
    19: "nineteen" , 20: "twenty" , 30: "thirty" , 40: "forty" , 50: "fifty" , 60: "sixty" , 70: "seventy" , 
    80: "eighty" , 90: "ninety", 100: "one hundred", 200: "two hundred", 300: "three hundred", 400: "four hundred", 500: "five hundred",
    600: "six hundred", 700: "seven hundred", 800: "eight hundred", 900: "nine hundred" } 


    #convert two digits numbers into words
    #if one is less than/equal to the user input or less than 19, print number 
    if 1 <= num <= 19: 
        print(number_dict[num])

    
    if 20 <= num <= 99: 
        n = num // 10 
        n2 = num % 10 
        if n == 1: 
            print(number_dict[num])
        else: 
            n *= 10 
            print(number_dict[n] , number_dict[n2])
        

numberconverter(num)