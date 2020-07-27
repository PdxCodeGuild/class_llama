from django.shortcuts import render

import random
import string

def index(request):
    pass

def shortenate():
    characters = string.ascii_letters + string.digits
    character_list = []
    for c in characters:
        character_list.append(c)

    secret_code = ""
    for i in range(1,6):
        new_char = random.choice(character_list)
        secret_code += new_char
    return secret_code