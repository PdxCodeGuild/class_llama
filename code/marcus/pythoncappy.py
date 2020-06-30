import codecs

from stegano import lsb

user_input = input('What would you like to encrypt?: ')
encoded = codecs.encode(user_input, 'rot_13')

secret = lsb.hide(, encoded)
secret.save()

clear_message = lsb.reveal()
decoded = codecs.decode(clear_message, 'rot_13')
print(decoded)