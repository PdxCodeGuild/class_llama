import string
import random

characters = string.ascii_letters + string.digits
character_list = []
for c in characters:
    character_list.append(c)

secret_code = ""
for i in range(1,6):
    new_char = random.choice(character_list)
    secret_code += new_char

print(secret_code)