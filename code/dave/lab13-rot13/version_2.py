"""
# Lab 13: ROT Cipher

Write a program that prompts the user for a string,
and encodes it with ROT^x. The user decides how many
positions to rotate. For each character, find the
corresponding character, add it to an output string.
Notice that there are 26 letters in the English language,
so encryption is the same as decryption.
"""

# create ROT13 function
def rot13():
    letters = "abcdefghijklmnopqrstuvwxyz"

    # prompt user to enter str
    str = input("Enter a word: ")

    # prompt user to enter rotation amount
    rot = int(input("Enter how many positions to rotate (1 to 25): "))
    encrypted = ""

    '''
    for loop that finds the character, adds 'rot' variable,
    then if over 26 (the number of letters in alphabet)
    modulus 26 gives the remainder which wraps back to beginning of list
    '''
    for char in str:
        encrypted += letters[(letters.find(char)+rot)%26]
    return encrypted

print(rot13())