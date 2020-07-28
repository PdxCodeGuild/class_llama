from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

import string

from .models import url

def index(request): 
    return render(request, 'form/index.html')


def get_convert(request): 


def redirect(request):
  get_url = url.objects.all()
    context = { 
        'get_url': url
    }
    return