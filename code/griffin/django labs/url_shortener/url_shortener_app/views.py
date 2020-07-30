from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

import random
import string

from .models import UrlCode

def index(request):
    return render(request, 'url_shortener_app/index.html')


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

def add(request):
    long_url = request.POST['long_url']
    short_url = shortenate()    
    UrlCode.objects.create(long_url = long_url, secret_code = short_url)    
    return render(request, 'url_shortener_app/index.html', {'new_link':UrlCode.objects.get(secret_code=short_url)})

def lookup(request, short_url):
    item_got = get_object_or_404(UrlCode, secret_code=short_url)    
    if item_got.long_url[0:7] == "http://":
        return HttpResponseRedirect(item_got.long_url)
    else:
        item_got.long_url = "http://" + item_got.long_url
        return HttpResponseRedirect(item_got.long_url)


  

