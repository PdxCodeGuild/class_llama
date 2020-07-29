from django.shortcuts import render, redirect
from .models import ShortUrl
from .forms import UrlForm
from .shortener import ShortenCode

# Create your views here.

def index(request, token):
    long_url = ShortUrl.objects.filter(short_code=token)[0]
    return redirect(long_url.long_url)

def submit(request):
    form = UrlForm(request.POST)
    info = ''
    if request.method == 'POST':
        if form.is_valid():
            NewUrl = form.save(commit=False)
            info = ShortenCode().issue_token()
            NewUrl.short_code = info
            NewUrl.save()
        else:
            form = UrlForm()
            info = 'Invalid URL'
    return render(request, 'shorturl/submit.html', {'form': form, 'info': info})

    