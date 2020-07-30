from django.shortcuts import render

# Create your views here.

chirps = [{'name': 'Dave', 'text': 'First chirp'},
          {'name': 'Steve', 'text': 'Second chirp'},]

def home(request):
    context = {'chirps': chirps}
    return render(request, 'posts/home.html', context)