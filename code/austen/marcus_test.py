import codecs
from stegano import lsb



clear_message = lsb.reveal("Lenna-testing12.png")
decoded = codecs.decode(clear_message, 'rot_13')
print(decoded)