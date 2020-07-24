# Lab 13

import string

def encrypt(input_string, amount):
    output_string = ""
    for letter in input_string:
        if letter in string.ascii_lowercase:
            output_string += string.ascii_lowercase[(string.ascii_lowercase.index(letter) + int(amount)) % 26]
        elif letter in string.ascii_uppercase:
            output_string += string.ascii_uppercase[(string.ascii_uppercase.index(letter) + int(amount)) % 26]
        # ignores punctuation
        else: 
            output_string += letter
    return output_string
    
print(encrypt(input("Type something: "), input("Encrypt by how much?: ")))






    





    

    #for letters in i[range(0, 26)]:
        

# letter_dict = {i : letter_list[i] for i in range(1,len(letter_list))}




'''
while True:
    entered = input("Enter a word or phrase you would like to encrypt: ")
    encrypt(entered)
    # if there's a numerical value here...
    if .isdigit() in str.split(entered):
        print("Error. Only letters, please.")
        break
'''











