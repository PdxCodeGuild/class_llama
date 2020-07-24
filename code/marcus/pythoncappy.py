import codecs
from stegano import lsb

user_input = input('What would you like to encrypt?: ')
translated = codecs.encode(user_input, 'rot_13')

secret = lsb.hide("Lenna.png", translated)
secret.save("Lenna-testing12.png")

clear_message = lsb.reveal("Lenna-testing12.png")
decoded = codecs.decode(clear_message, 'rot_13')
print(decoded)