from playground import *
import codecs
from stegano import lsb
stuff = superspystuff(store)
# user_input = input('What would you like to encrypt?: ')
# translated = .encode(user_input, 'rot_13')
print(stuff)
secret = lsb.hide("Lenna.png", stuff)
secret.save("Lenna-testing12.png")

clear_message = lsb.reveal("Lenna-testing12.png")
decoder = decode(clear_message,store)
print(decoder)
