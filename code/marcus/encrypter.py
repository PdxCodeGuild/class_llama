from playground import *
import codecs
from stegano import lsb
stuff, num1 = superspystuff()
# user_input = input('What would you like to encrypt?: ')
# translated = .encode(user_input, 'rot_13')

secret = lsb.hide("Lenna.png", stuff)
secret.save("Lenna-testing123.png")

clear_message = lsb.reveal("Lenna-testing123.png")
decoder = decode(clear_message,num1)
# print(decoder)
