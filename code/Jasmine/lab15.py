''' 
convert a number into plain word (i.e. sixty-seven for 67). 
function must be able to convert 0-99 

Hint: you can use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10

Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.
''' 

num = int(input("Pick a number: "))


def convert_nums(num):
    #create a dictionary where the key is a number and the value is a string
    number_dict = {1: "one" , 2: "two" , 3: "three" , 4: "four" , 5: "5" , 
    6: "6" , 7: "seven" , 8: "eight" , 9: "nine" , 10: "ten" , 11: "eleven" , 12: "twelve" ,  
    13: "thirteen" , 14: "fourteen" , 15: "fifteen" , 16: "sixteen" , 17: "seventeen" , 18: "eighteen" , 
    19: "nineteen" , 20: "twenty" , 30: "thirty" , 40: "forty" , 50: "fifty" , 60: "sixty" , 70: "seventy" , 80: "eighty" , 90: "ninety"} 


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
        #print(n)
        #print(n2)
        #print(number_dict[num])
        

convert_nums(num)