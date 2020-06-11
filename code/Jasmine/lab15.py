''' 
convert a number into plain word (i.e. sixty-seven for 67). 
function must be able to convert 0-99 

Hint: you can use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10

Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.
''' 

num = int(input("What is your number: "))

def convert_nums()
    #create a dictionary where the key is a number and the value is a string