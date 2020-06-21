'''
lab 13: ROT13

''' 

import string

def rot13(input_string):
    output = ""
    for letter in input_string: 
        if letter in string.ascii_lowercase:
            output += string.ascii_lowercase[(string.ascii_lowercase.index(letter) + 13) % 26]
        elif letter in string.ascii_uppercase:
            output += string.ascii_uppercase[(string.ascii_uppercase.index(letter) + 13) % 26]
        else: 
            output += letter
    return output

print(rot13(input("Enter some letters:")))