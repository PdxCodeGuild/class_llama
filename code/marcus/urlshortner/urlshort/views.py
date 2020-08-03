from django.shortcuts import render, get_object_or_404
from .models import Url_shortner
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
import random
import string


def url_short(request):
    letters = string.ascii_lowercase
    numbers = range(0,9)

    shortener = (random.choice(letters) + random.choice(numbers)) for i in range(6)
    

        


# Create your views here.
