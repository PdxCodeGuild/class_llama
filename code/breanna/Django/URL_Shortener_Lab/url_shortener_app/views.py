from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import string
from random import choice

def shorten():
    letters = random.choice(string.ascii_letters)
    digits = random.choice(string.digits)

    for x in range(6):
        short_url = random.choice(choice(letters) + choice(digits))

    return(short_url)

def index(request):
    return render(request, 'url_shortener/index.html')

def submit_url(request):
    UrlShortener.objects.create(long_url=request.POST['long_url'], short_url=shorten())
    
    context = {
        'context': context_context
    }
    return render(request, 'url_shortener/index.html', context)

def redirect(request, short_url):
    url = get_object_or_404(UrlShortener, short_url=short_url)
    return HttpResponseRedirect(url.long_url)
