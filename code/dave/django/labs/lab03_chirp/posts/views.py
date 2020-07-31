from django.shortcuts import render

from .models import Chirps

# Create your views here.

''' 
 # used list for testing
 chirps = [{'name': 'Dave', 'text': 'First chirp'},
           {'name': 'Steve', 'text': 'Second chirp'},] 
'''

def home(request):
    context = {'chirps': Chirps.objects.all()}
    return render(request, 'posts/home.html', context)