
# Practice: Strings

# PROBLEM 1

# Get a string from the user,
# print out another string,
# doubling every letter
def double_letters():
    
    # get user input
    input_string = input("Type something here: ")
    return ''.join([x*2 for x in input_string])

print(double_letters())

# PROBLEM 2
# Write a func that takes a string,
# and returns a list of strings, 
# each missing a different character.

def missing_char(str):

    # initialize list
    list = []

    # add each char of the string to list as individual chars ie: ['h','e','l','l','o']
    list[:0] = str
    return list

print(missing_char('hello'))