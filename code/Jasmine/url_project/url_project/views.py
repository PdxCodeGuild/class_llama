from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

import string, random

from .models import url

def index(request): 
    return render(request, 'form/index.html')


def convert(request): 
    long_url = request.POST['get_url']
    short_url = ''
    for x in range(6): 
        short_url+= random.choice(string.ascii_letters)
    url.objects.create(long_url= long_url, short_url = short_url)
    return render (request , 'form/index.html', {'short_url': url.objects.get(short_url=short_url)})

def redirect(request, short_url):
   redirect_url = get_object_or_404(url,short_url=short_url)
   return HttpResponseRedirect(redirect_url.long_url)