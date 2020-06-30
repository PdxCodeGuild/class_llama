import codecs

def translator():
    user_input = input('What would you like to encrypt?: ')
    translated = codecs.encode(user_input, 'rot_13')
    print(translated)
translator()