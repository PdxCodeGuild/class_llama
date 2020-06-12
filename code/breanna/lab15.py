# Number to Phrase

og_num = int(input("Pick a number between 1 and 99: "))

def num_to_word(num):
   
    # create dictionary, key is number and value is string of number written out
    # write ones numbers, teens to avoid issues with tens and ones space, and tens numbers
    num_dict = {1: "one" , 2: "two" , 3: "three" , 4: "four" , 5: "5" , 
    6: "6" , 7: "seven" , 8: "eight" , 9: "nine" , 10: "ten" , 11: "eleven" , 12: "twelve" ,  
    13: "thirteen" , 14: "fourteen" , 15: "fifteen" , 16: "sixteen" , 17: "seventeen" , 18: "eighteen" , 
    19: "nineteen" , 20: "twenty" , 30: "thirty" , 40: "forty" , 50: "fifty" , 60: "sixty" , 70: "seventy" , 
    80: "eighty" , 90: "ninety"} 
    
    # avoid issue with teens by including here
    if 1 <= og_num <= 19: 
        print(num_dict[og_num])
    
    # the rest will use tens and ones words
    if 20 <= og_num <= 99: 
        
        n1 = og_num // 10 
        n2 = og_num % 10 
        
        # find the tens word
        if n1 == 1: 
            print(num_dict[og_num])
        # find the ones word
        else: 
            n1 *= 10 
            print(num_dict[n1] , num_dict[n2])

num_to_word(og_num)