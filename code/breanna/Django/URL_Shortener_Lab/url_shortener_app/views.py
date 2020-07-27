from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import string
from random import choice

def submit_url(request):
    long_url = ''
    return long_url

def redirect(request):
    return HttpResponse('ok')

def shorten(self):
    letters = random.choice(string.ascii_letters)
    digits = random.choice(string.digits)

    for x in range(6):
        short_url = random.choice(choice(letters) + choice(digits))

    return(short_url)