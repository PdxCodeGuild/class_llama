from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
import string
import random
from .models import UrlShortener

def shorten():
    letters = string.ascii_letters
    short_url = ''

    for x in range(6):
        short_url += random.choice(letters)

    return(short_url)

def index(request):
    return render(request, 'url_shortener/index.html')

def submit_url(request):
    url = UrlShortener.objects.create(long_url=request.POST['long_url'], short_url=shorten())
    
    context = {
        'short_url': url.short_url
    }
    return render(request, 'url_shortener/index.html', context)

def redirect(request, short_url):
    url = get_object_or_404(UrlShortener, short_url=short_url)
    return HttpResponseRedirect(url.long_url)
