from django.shortcuts import render
from .models import Post

def home(request):
    return render(request, 'posts/home.html')