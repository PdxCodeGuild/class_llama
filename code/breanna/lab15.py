# Number to Phrase

og_num = int(input("Pick a number between 1 and 999: "))

def num_to_word(num):
   
    # create dictionary, key is number and value is string of number written out
    # write ones, teens to avoid issues with tens and ones space, tens, hundreds
    num_dict = {1: "one" , 2: "two" , 3: "three" , 4: "four" , 5: "five" , 
    6: "six" , 7: "seven" , 8: "eight" , 9: "nine" , 10: "ten" , 11: "eleven" , 12: "twelve" ,  
    13: "thirteen" , 14: "fourteen" , 15: "fifteen" , 16: "sixteen" , 17: "seventeen" , 18: "eighteen" , 
    19: "nineteen" , 20: "twenty" , 30: "thirty" , 40: "forty" , 50: "fifty" , 60: "sixty" , 70: "seventy" , 
    80: "eighty" , 90: "ninety" , 100: "one hundred", 200: "two hundred", 300: "three hundred", 400: "four hundred", 500: "five hundred",
    600: "six hundred", 700: "seven hundred", 800: "eight hundred", 900: "nine hundred"} 
    
    # avoid issue with teens by including here
    if 1 <= og_num <= 19: 
        print(num_dict[og_num])
    
    # get tens and ones words
    if 20 <= og_num <= 99: 
        
        n1 = og_num // 10 
        n2 = og_num % 10 
        
        # find the tens word
        if n1 == 1: 
            print(num_dict[og_num])
        # find the tens word then ones word
        else: 
            n1 *= 10 
            print(num_dict[n1] , num_dict[n2])

    # get hundreds word
    if 100 <= og_num <= 999:

        # floor divide for hundreds
        n1 = og_num // 100
        # modulus to take away hundreds then floor divide remainder for tens
        n2 = og_num % 100 // 10
        n3 = og_num % 10

        # get the ones
        if n1 == 0 and n2 == 0 and n3 == 1:
            print(num_dict[og_num])
        # get the tens
        elif n1 == 0 and n2 == 1 and n3 == 1:
            n2 *= 10
            print(num_dict[n1] , num_dict[n2])
        # get the hundreds
        else:
            n1 *= 100
            n2 *= 10
            # print(n1, n2, n3)
            print(num_dict[n1] , num_dict[n2] , num_dict[n3])

num_to_word(og_num)
