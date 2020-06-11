"""
# Lab 13: ROT Cipher

Write a program that prompts the user for a string, 
and encodes it with ROT13. For each character, find the 
corresponding character, add it to an output string. 
Notice that there are 26 letters in the English language, 
so encryption is the same as decryption.
"""

# create ROT13 function
def rot13():
    letters = "abcdefghijklmnopqrstuvwxyz"
    str = input("Enter a word: ")
    encrypted = ""

    # prompt user to enter str

    # for loop that finds the character, adds 13, 
    # then if over 26 (the number of letters in alphabet)
    # modulus 26 gives the remainder which wraps back to beginning of list
    for char in str:
        encrypted += letters[(letters.find(char)+13)%26]
    return encrypted

print(rot13())